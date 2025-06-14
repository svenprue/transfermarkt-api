from dataclasses import dataclass

from app.services.base import TransfermarktBase
from app.utils.regex import REGEX_DOB
from app.utils.utils import extract_from_url, safe_regex
from app.utils.xpath import Clubs


@dataclass
class TransfermarktClubPlayers(TransfermarktBase):
    """
    A class for retrieving and parsing the players of a football club or national team from Transfermarkt.

    Args:
        club_id (str): The unique identifier of the football club or national team.
        season_id (str): The unique identifier of the season.
        is_national (bool): Flag indicating if this is a national team.
        URL (str): The URL template for the club's players page on Transfermarkt.
    """

    club_id: str = None
    season_id: str = None
    is_national: bool = False
    URL: str = "https://www.transfermarkt.com/-/kader/verein/{club_id}/saison_id/{season_id}/plus/1"

    def __post_init__(self) -> None:
        """Initialize the TransfermarktClubPlayers class."""
        self.URL = self.URL.format(club_id=self.club_id, season_id=self.season_id)
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath=Clubs.Players.CLUB_NAME)
        self.__update_season_id()
        self.__update_past_flag()

    def __update_season_id(self):
        """Update the season ID if it's not provided by extracting it from the website."""
        if self.season_id is None:
            self.season_id = extract_from_url(self.get_text_by_xpath(Clubs.Players.CLUB_URL), "season_id")

    def __update_past_flag(self) -> None:
        """Check if the season is the current or if it's a past one and update the flag accordingly."""
        self.past = "Current club" in self.get_list_by_xpath(Clubs.Players.PAST_FLAG)

    def __parse_national_team_players(self) -> list[dict]:
        """
        Parse player information for national teams from the webpage.

        Returns:
            list[dict]: A list of player information dictionaries.
        """
        # Extract player rows for context
        player_rows = self.page.xpath(Clubs.NationalPlayers.PLAYER_ROWS)

        # Get basic player information
        players_ids = [extract_from_url(url) for url in self.get_list_by_xpath(Clubs.NationalPlayers.URLS)]
        players_names = self.get_list_by_xpath(Clubs.NationalPlayers.NAMES)
        players_positions = self.get_list_by_xpath(Clubs.NationalPlayers.POSITIONS)

        # Get DOB and age information
        dob_age_data = self.get_list_by_xpath(Clubs.NationalPlayers.DOB_AGE)
        players_dobs = [safe_regex(dob_age, REGEX_DOB, "dob") for dob_age in dob_age_data]
        players_ages = [safe_regex(dob_age, REGEX_DOB, "age") for dob_age in dob_age_data]

        # For national teams, every player has the nationality of the team
        players_nationalities = [[] for _ in range(len(players_ids))]

        # Get club information
        players_current_club = self.get_list_by_xpath(Clubs.NationalPlayers.CURRENT_CLUBS)

        # Get physical attributes
        players_heights = self.get_list_by_xpath(Clubs.NationalPlayers.HEIGHTS)
        players_foots = self.get_list_by_xpath(Clubs.NationalPlayers.FOOTS, remove_empty=False)

        # Get national team statistics
        players_intl_matches = self.get_list_by_xpath(Clubs.NationalPlayers.INTERNATIONAL_MATCHES)
        players_goals = self.get_list_by_xpath(Clubs.NationalPlayers.GOALS)

        # Get debut dates using row-by-row approach for more reliability
        players_joined_on = []
        for row in player_rows:
            debut = row.xpath(Clubs.NationalPlayers.WithinRow.DEBUT)
            players_joined_on.append(debut[0] if debut else "")

        # Set national team specific fields
        players_joined = ["National Team Debut"] * len(players_ids)
        players_signed_from = [""] * len(players_ids)
        players_contracts = [""] * len(players_ids)

        # Get market values
        players_marketvalues = self.get_list_by_xpath(Clubs.NationalPlayers.MARKET_VALUES)

        # Get player statuses
        players_statuses = []
        for row in player_rows:
            status = row.xpath(Clubs.NationalPlayers.WithinRow.STATUS)
            players_statuses.append("; ".join(status) if status else "")

        return [
            {
                "id": idx,
                "name": name,
                "position": position,
                "dateOfBirth": dob,
                "age": age,
                "nationality": nationality,
                "currentClub": current_club,
                "height": height,
                "foot": foot,
                "internationalMatches": intl_matches,
                "goals": goals,
                "joinedOn": joined_on,
                "joined": joined,
                "signedFrom": signed_from,
                "contract": contract,
                "marketValue": market_value,
                "status": status,
            }
            for
            idx, name, position, dob, age, nationality, current_club, height, foot, intl_matches, goals, joined_on, joined, signed_from, contract, market_value, status
            in zip(
                players_ids,
                players_names,
                players_positions,
                players_dobs,
                players_ages,
                players_nationalities,
                players_current_club,
                players_heights,
                players_foots,
                players_intl_matches,
                players_goals,
                players_joined_on,
                players_joined,
                players_signed_from,
                players_contracts,
                players_marketvalues,
                players_statuses,
            )
        ]

    def __parse_club_players(self) -> list[dict]:
        """
        Parse player information for regular clubs from the webpage.

        Returns:
            list[dict]: A list of player information dictionaries.
        """
        page_nationalities = self.page.xpath(Clubs.Players.PAGE_NATIONALITIES)
        page_players_infos = self.page.xpath(Clubs.Players.PAGE_INFOS)
        page_players_signed_from = self.page.xpath(
            Clubs.Players.Past.PAGE_SIGNED_FROM if self.past else Clubs.Players.Present.PAGE_SIGNED_FROM,
        )
        page_players_joined_on = self.page.xpath(
            Clubs.Players.Past.PAGE_JOINED_ON if self.past else Clubs.Players.Present.PAGE_JOINED_ON,
        )
        players_ids = [extract_from_url(url) for url in self.get_list_by_xpath(Clubs.Players.URLS)]
        players_names = self.get_list_by_xpath(Clubs.Players.NAMES)
        players_positions = self.get_list_by_xpath(Clubs.Players.POSITIONS)
        players_dobs = [
            safe_regex(dob_age, REGEX_DOB, "dob") for dob_age in self.get_list_by_xpath(Clubs.Players.DOB_AGE)
        ]
        players_ages = [
            safe_regex(dob_age, REGEX_DOB, "age") for dob_age in self.get_list_by_xpath(Clubs.Players.DOB_AGE)
        ]
        players_nationalities = [nationality.xpath(Clubs.Players.NATIONALITIES) for nationality in page_nationalities]
        players_current_club = (
            self.get_list_by_xpath(Clubs.Players.Past.CURRENT_CLUB) if self.past else [None] * len(players_ids)
        )
        players_heights = self.get_list_by_xpath(
            Clubs.Players.Past.HEIGHTS if self.past else Clubs.Players.Present.HEIGHTS,
        )
        players_foots = self.get_list_by_xpath(
            Clubs.Players.Past.FOOTS if self.past else Clubs.Players.Present.FOOTS,
            remove_empty=False,
        )
        players_joined_on = ["; ".join(e.xpath(Clubs.Players.JOINED_ON)) for e in page_players_joined_on]
        players_joined = ["; ".join(e.xpath(Clubs.Players.JOINED)) for e in page_players_infos]
        players_signed_from = ["; ".join(e.xpath(Clubs.Players.SIGNED_FROM)) for e in page_players_signed_from]
        players_contracts = (
            [None] * len(players_ids) if self.past else self.get_list_by_xpath(Clubs.Players.Present.CONTRACTS)
        )
        players_marketvalues = self.get_list_by_xpath(Clubs.Players.MARKET_VALUES)
        players_statuses = ["; ".join(e.xpath(Clubs.Players.STATUSES)) for e in page_players_infos if e is not None]

        return [
            {
                "id": idx,
                "name": name,
                "position": position,
                "dateOfBirth": dob,
                "age": age,
                "nationality": nationality,
                "currentClub": current_club,
                "height": height,
                "foot": foot,
                "joinedOn": joined_on,
                "joined": joined,
                "signedFrom": signed_from,
                "contract": contract,
                "marketValue": market_value,
                "status": status,
            }
            for
            idx, name, position, dob, age, nationality, current_club, height, foot, joined_on, joined, signed_from, contract, market_value, status,
            in zip(
                players_ids,
                players_names,
                players_positions,
                players_dobs,
                players_ages,
                players_nationalities,
                players_current_club,
                players_heights,
                players_foots,
                players_joined_on,
                players_joined,
                players_signed_from,
                players_contracts,
                players_marketvalues,
                players_statuses,
            )
        ]

    def get_club_players(self) -> dict:
        """
        Retrieve and parse player information for the specified football club or national team.

        Returns:
            dict: A dictionary containing the club's unique identifier, is_national flag,
                  player information, and the timestamp of when the data was last updated.
        """
        self.response["id"] = self.club_id
        self.response["isNational"] = self.is_national

        if self.is_national:
            self.response["players"] = self.__parse_national_team_players()
        else:
            self.response["players"] = self.__parse_club_players()

        return self.response