from dataclasses import dataclass

from app.services.base import TransfermarktBase
from app.utils.utils import safe_regex, extract_from_url
from app.utils.xpath import Clubs


@dataclass
class TransfermarktClubManagers(TransfermarktBase):
    """
    A class for retrieving and parsing the managers of a football club from Transfermarkt.

    Args:
        club_id (str): The unique identifier of the football club.
        URL (str): The URL template for the club's managers history page on Transfermarkt.
    """

    club_id: str = None
    URL: str = "https://www.transfermarkt.com/-/mitarbeiterhistorie/verein/{club_id}/personalie_id/1"

    def __post_init__(self) -> None:
        """Initialize the TransfermarktClubManagers class."""
        self.URL = self.URL.format(club_id=self.club_id)
        self.page = self.request_url_page()

    def __parse_club_managers(self) -> list[dict]:
        """
        Parse manager information from the webpage and return a list of dictionaries,
        each representing a manager.

        Returns:
            list[dict]: A list of manager information dictionaries.
        """
        rows = self.page.xpath(Clubs.Managers.ROWS)
        valid_rows = [row for row in rows if row.xpath(Clubs.Managers.NAME)]

        manager_names = [row.xpath(Clubs.Managers.NAME)[0] if row.xpath(Clubs.Managers.NAME) else "" for row in
                         valid_rows]

        manager_links = [row.xpath(Clubs.Managers.PROFILE_URL)[0] if row.xpath(Clubs.Managers.PROFILE_URL) else "" for
                         row in valid_rows]

        manager_ids = [safe_regex(link, Clubs.Managers.ID, "id") for link in manager_links]

        nationalities = [row.xpath(Clubs.Managers.NATIONALITY) for row in valid_rows]
        manager_nationalities = ["; ".join(nationality) for nationality in nationalities]

        start_dates = [row.xpath(Clubs.Managers.APPOINTED)[0] if row.xpath(Clubs.Managers.APPOINTED) else "" for row in
                       valid_rows]

        end_dates = [row.xpath(Clubs.Managers.END_DATE)[0] if row.xpath(Clubs.Managers.END_DATE) else "" for row in
                     valid_rows]

        time_in_office = [row.xpath(Clubs.Managers.TIME_IN_POST)[0] if row.xpath(Clubs.Managers.TIME_IN_POST) else ""
                          for row in valid_rows]
        games = [row.xpath(Clubs.Managers.MATCHES)[0] if row.xpath(Clubs.Managers.MATCHES) else "" for row in
                 valid_rows]

        points_per_game = [row.xpath(Clubs.Managers.PPG)[0] if row.xpath(Clubs.Managers.PPG) else "" for row in
                           valid_rows]

        return [
            {
                "id": manager_id,
                "name": name,
                "nationality": nationality,
                "startDate": start_date,
                "endDate": end_date,
                "timeInOffice": time_in_office_val,
                "games": games_val,
                "pointsPerGame": ppg_val
            }
            for manager_id, name, nationality, start_date, end_date, time_in_office_val, games_val, ppg_val in zip(
                manager_ids,
                manager_names,
                manager_nationalities,
                start_dates,
                end_dates,
                time_in_office,
                games,
                points_per_game
            )
            if name and manager_id
        ]

    def get_club_managers(self) -> dict:
        """
        Retrieve and parse manager information for the specified football club.

        Returns:
            dict: A dictionary containing the club's unique identifier and manager information.
        """
        self.response["id"] = self.club_id
        self.response["managers"] = self.__parse_club_managers()
        return self.response