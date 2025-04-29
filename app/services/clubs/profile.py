from dataclasses import dataclass

from app.services.base import TransfermarktBase
from app.utils.regex import REGEX_BG_COLOR, REGEX_COUNTRY_ID, REGEX_MEMBERS_DATE
from app.utils.utils import extract_from_url, remove_str, safe_regex, safe_split
from app.utils.xpath import Clubs


@dataclass
class TransfermarktClubProfile(TransfermarktBase):
    """
    A class for retrieving and parsing the profile information of a football club from Transfermarkt.

    Args:
        club_id (str): The unique identifier of the football club.
        URL (str): The URL template for the club's profile page on Transfermarkt.
    """

    club_id: str = None
    URL: str = "https://www.transfermarkt.us/-/datenfakten/verein/{club_id}"

    def __post_init__(self) -> None:
        """Initialize the TransfermarktClubProfile class."""
        self.URL = self.URL.format(club_id=self.club_id)
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath=Clubs.Profile.URL)

    def get_club_profile(self) -> dict:
        """
        Retrieve and parse the profile information of the football club from Transfermarkt.

        This method extracts various attributes of the club's profile, such as name, official name, address, contact
        information, stadium details, and more.

        Returns:
            dict: A dictionary containing the club's profile information.
        """
        self.response["id"] = self.club_id
        self.response["url"] = self.get_text_by_xpath(Clubs.Profile.URL)
        self.response["name"] = self.get_text_by_xpath(Clubs.Profile.NAME)
        self.response["officialName"] = self.get_text_by_xpath(Clubs.Profile.NAME_OFFICIAL)
        self.response["image"] = safe_split(self.get_text_by_xpath(Clubs.Profile.IMAGE), "?")[0]
        self.response["foundedOn"] = self.get_text_by_xpath(Clubs.Profile.FOUNDED_ON)
        self.response["currentMarketValue"] = self.get_text_by_xpath(
            Clubs.Profile.MARKET_VALUE,
            iloc_to=3,
            join_str="",
        )
        self.response["confederation"] = self.get_text_by_xpath(Clubs.Profile.CONFEDERATION)
        self.response["isNational"] = True if self.response["confederation"] == "UEFA" else False
        self.response["fifaWorldRanking"] = remove_str(self.get_text_by_xpath(Clubs.Profile.RANKING), "Pos")
        self.response["league"] = {
            "id": extract_from_url(self.get_text_by_xpath(Clubs.Profile.LEAGUE_ID)),
            "name": self.get_text_by_xpath(Clubs.Profile.LEAGUE_NAME),
            "countryId": safe_regex(self.get_text_by_xpath(Clubs.Profile.LEAGUE_COUNTRY_ID), REGEX_COUNTRY_ID, "id"),
            "countryName": self.get_text_by_xpath(Clubs.Profile.LEAGUE_COUNTRY_NAME),
            "tier": self.get_text_by_xpath(Clubs.Profile.LEAGUE_TIER),
        }
        return self.response
