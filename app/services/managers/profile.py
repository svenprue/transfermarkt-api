from dataclasses import dataclass
from datetime import datetime

from app.services.base import TransfermarktBase
from app.utils.regex import REGEX_DOB_AGE, REGEX_PLAYER_ID, REGEX_CLUB_ID, REGEX_MANAGER_ID, REGEX_DATE_FORMAT
from app.utils.utils import extract_from_url, safe_regex, trim
from app.utils.xpath import Managers


@dataclass
class TransfermarktManagerProfile(TransfermarktBase):
    """
    Represents a service for retrieving and parsing the profile information of a football manager on Transfermarkt.

    Args:
        manager_id (str): The unique identifier of the manager.

    Attributes:
        URL (str): The URL to fetch the manager's profile data.
    """

    manager_id: str = None
    URL: str = "https://www.transfermarkt.com/-/profil/trainer/{manager_id}"
    base_url: str = "https://www.transfermarkt.com"

    def __post_init__(self) -> None:
        """Initialize the TransfermarktManagerProfile class."""
        self.URL = self.URL.format(manager_id=self.manager_id)
        self.page = self.request_url_page()

    def __get_citizenship(self) -> list:
        """
        Parse the citizenship information which may contain multiple nationalities.

        Returns:
            list: A list of citizenship countries
        """
        citizenship_element = self.page.xpath(Managers.ManagerProfile.CITIZENSHIP)
        if not citizenship_element:
            return []

        # Look for img elements with country flags and get their titles
        citizenships = []
        for element in citizenship_element:
            # Get text nodes for countries listed as text
            text_citizenships = element.xpath("text()").strip() if hasattr(element.xpath("text()"), "strip") else ""
            if text_citizenships:
                citizenships.extend([c.strip() for c in text_citizenships.split(",")])

            # Get country flags
            flag_citizenships = element.xpath(".//img/@title")
            citizenships.extend(flag_citizenships)

        return [c for c in citizenships if c]  # Filter out empty strings

    def __parse_player_profile(self) -> dict:
        """
        Parse the player profile information if the manager was a former player.

        Returns:
            dict: Dictionary containing player profile information or None if not a former player
        """
        is_former_player = self.page.xpath(Managers.ManagerProfile.IS_FORMER_PLAYER)

        if not is_former_player:
            return None

        player_url = self.get_text_by_xpath(Managers.ManagerProfile.PLAYER_URL)
        player_id = safe_regex(player_url, REGEX_PLAYER_ID, "player_id") if player_url else None
        retired_on_text = self.get_text_by_xpath(Managers.ManagerProfile.RETIRED_ON)
        retired_on = safe_regex(retired_on_text, REGEX_DATE_FORMAT, "date") if retired_on_text else None
        player_url = self.base_url + player_url

        return {
            "id": player_id,
            "url": player_url,
            "retired": retired_on is not None,
            "retiredSince": retired_on
        }

    def __parse_club_info(self) -> dict:
        """
        Parse the current club information of the manager.

        Returns:
            dict: Dictionary containing club information or None if no current club
        """
        club_name = self.get_text_by_xpath(Managers.ManagerProfile.CLUB_NAME)

        if not club_name:
            return None

        club_id_url = self.get_text_by_xpath(Managers.ManagerProfile.CLUB_ID)
        club_id = safe_regex(club_id_url, REGEX_CLUB_ID, "club_id") if club_id_url else None
        club_role = self.get_text_by_xpath(Managers.ManagerProfile.CLUB_ROLE)
        start_date_text = self.get_text_by_xpath(Managers.ManagerProfile.CLUB_START_DATE)
        end_date_text = self.get_text_by_xpath(Managers.ManagerProfile.CLUB_END_DATE)

        start_date = safe_regex(start_date_text, REGEX_DATE_FORMAT, "date") if start_date_text else None
        end_date = safe_regex(end_date_text, REGEX_DATE_FORMAT, "date") if end_date_text else None

        return {
            "id": club_id,
            "name": club_name,
            "role": club_role,
            "startDate": start_date,
            "endDate": end_date
        }

    def get_manager_profile(self) -> dict:
        """
        Retrieve and parse the manager's profile information, including their personal details,
        club affiliation, and player profile if they are former players.

        Returns:
            dict: A dictionary containing the manager's unique identifier, profile information, and the timestamp of when
                the data was last updated.
        """

        self.response["id"] = self.manager_id
        self.response["url"] = self.get_text_by_xpath(Managers.ManagerProfile.PROFILE_URL)

        # Get name components and construct full name
        name_first = self.get_text_by_xpath(Managers.ManagerProfile.NAME_FIRST)
        name_last = self.get_text_by_xpath(Managers.ManagerProfile.NAME_LAST)
        self.response["name"] = f"{name_first} {name_last}".strip()

        # Get full name if available
        full_name_element = self.page.xpath(Managers.ManagerProfile.FULL_NAME)
        full_name = " ".join([node.strip() for node in full_name_element[0].xpath(".//text()") if
                              node.strip()]) if full_name_element else None
        self.response["fullName"] = full_name

        # Get image URL
        self.response["imageUrl"] = self.get_text_by_xpath(Managers.ManagerProfile.IMAGE_URL)

        # Get date of birth and age
        dob_age = self.get_text_by_xpath(Managers.ManagerProfile.DOB_AND_AGE)
        self.response["dateOfBirth"] = safe_regex(dob_age, REGEX_DOB_AGE, "dob") if dob_age else None
        self.response["age"] = safe_regex(dob_age, REGEX_DOB_AGE, "age") if dob_age else None

        # Get place of birth
        self.response["placeOfBirth"] = {
            "city": self.get_text_by_xpath(Managers.ManagerProfile.PLACE_OF_BIRTH_CITY),
            "country": self.get_text_by_xpath(Managers.ManagerProfile.PLACE_OF_BIRTH_COUNTRY)
        }

        # Get citizenship
        self.response["citizenship"] = self.__get_citizenship()

        # Get club information
        self.response["club"] = self.__parse_club_info()

        # Get player profile if the manager was a former player
        self.response["playerProfile"] = self.__parse_player_profile()

        return self.response