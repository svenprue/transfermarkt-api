from dataclasses import dataclass

from app.services.base import TransfermarktBase
from app.utils.utils import extract_from_url
from app.utils.xpath import Competitions


@dataclass
class TransfermarktCompetitionClubs(TransfermarktBase):
    """
    A class for retrieving and parsing the list of football clubs in a specific competition on Transfermarkt.

    Args:
        competition_id (str): The unique identifier of the competition.
        season_id (str): The season identifier. If not provided, it will be extracted from the URL.
        URL (str): The URL template for the competition's page on Transfermarkt.
    """

    competition_id: str = None
    season_id: str = None
    is_knockout: bool = False
    URL: str = "https://www.transfermarkt.com/-/startseite/wettbewerb/{competition_id}/plus/?saison_id={season_id}"
    URL_knockout: str = "https://www.transfermarkt.com/-/teilnehmer/pokalwettbewerb/{competition_id}/saison_id/{season_id}"

    def __post_init__(self) -> None:
        """Initialize the TransfermarktCompetitionClubs class."""
        if not self.is_knockout:
            self.URL = self.URL.format(competition_id=self.competition_id, season_id=self.season_id)
        else:
            self.URL = self.URL_knockout.format(competition_id=self.competition_id, season_id=self.season_id)
        self.page = self.request_url_page()

    def __parse_competition_clubs(self) -> list:
        """
        Parse the competition's page and extract information about the football clubs participating
            in the competition.

        Returns:
            list: A list of dictionaries, where each dictionary contains information about a
                football club in the competition, including the club's unique identifier and name.
        """
        if self.is_knockout:
            # Primary XPath selector for knockout format
            urls = self.get_list_by_xpath(Competitions.Clubs.KNOCKOUT_URLS)
            names = self.get_list_by_xpath(Competitions.Clubs.KNOCKOUT_NAMES)

            # If primary selectors return empty results, try backup selectors
            if not urls:
                urls = self.get_list_by_xpath("//td[@class='links no-border-links hauptlink']/a/@href")
                names = self.get_list_by_xpath("//td[@class='links no-border-links hauptlink']/a/text()")
        else:
            # Regular competition format
            urls = self.get_list_by_xpath(Competitions.Clubs.URLS)
            names = self.get_list_by_xpath(Competitions.Clubs.NAMES)

        ids = [extract_from_url(url) for url in urls]
        print(urls)
        return [{"id": idx, "name": name} for idx, name in zip(ids, names)]

    def get_competition_clubs(self) -> dict:
        """
        Retrieve and parse the list of football clubs participating in a specific competition.

        Returns:
            dict: A dictionary containing the competition's unique identifier, name, season identifier, list of clubs
                  participating in the competition, and the timestamp of when the data was last updated.
        """
        self.response["id"] = self.competition_id
        self.response["name"] = self.get_text_by_xpath(Competitions.Profile.KNOCKOUT_NAME if self.is_knockout else Competitions.Profile.NAME)
        self.response["seasonId"] = self.season_id
        self.response["isKnockout"] = self.is_knockout
        self.response["clubs"] = self.__parse_competition_clubs()
        return self.response
