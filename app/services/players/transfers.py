from dataclasses import dataclass
import logging

from app.services.base import TransfermarktBase
from app.utils.utils import extract_from_url, safe_split
from app.utils.xpath import Players


@dataclass
class TransfermarktPlayerTransfers(TransfermarktBase):
    """
    A class for retrieving and parsing the player's transfer history and youth club details from Transfermarkt.

    Args:
        player_id (str): The unique identifier of the player.
        URL (str): The URL template for the player's transfers page on Transfermarkt.
    """

    player_id: str = None
    URL: str = "https://www.transfermarkt.com/-/transfers/spieler/{player_id}"
    URL_TRANSFERS: str = "https://www.transfermarkt.com/ceapi/transferHistory/list/{player_id}"

    def __post_init__(self) -> None:
        """Initialize the TransfermarktPlayerTransfers class."""
        self.URL = self.URL.format(player_id=self.player_id)
        self.page = self.request_url_page()
        self.raise_exception_if_not_found(xpath=Players.Profile.NAME)
        self.transfer_history = self.make_request(url=self.URL_TRANSFERS.format(player_id=self.player_id))

    def __parse_player_transfer_history(self) -> list:
        """
        Parse and retrieve the transfer history of the specified player from Transfermarkt,
        including the unique identifier of each transfer, source club information (ID and name),
        destination club information (ID and name), transfer date, upcoming status, season, market
        value at the time of transfer, and transfer fee.

        Returns:
            list: A list of dictionaries, each containing details of the player's transfer history,
        """
        transfers = self.transfer_history.json().get("transfers", [])
        result = []

        for i, transfer in enumerate(transfers):
            try:
                # Use original extract_from_url function but handle potential errors
                transfer_id = extract_from_url(transfer["url"], "transfer_id")

                # Handle club IDs safely
                from_club_id = None
                to_club_id = None

                if transfer["from"]["href"]:
                    from_club_id = extract_from_url(transfer["from"]["href"])

                if transfer["to"]["href"]:
                    to_club_id = extract_from_url(transfer["to"]["href"])

                # Handle empty or invalid dates
                date = transfer["date"]
                if not date or date == "0000-00-00":
                    date = None

                # Standardize fee values
                fee = transfer["fee"]
                if fee in ["-", "?", "free transfer"]:
                    fee = ""

                # Create transfer record
                transfer_record = {
                    "id": transfer_id,
                    "clubFrom": {
                        "id": from_club_id,
                        "name": transfer["from"]["clubName"],
                    },
                    "clubTo": {
                        "id": to_club_id,
                        "name": transfer["to"]["clubName"],
                    },
                    "date": date,
                    "upcoming": transfer["upcoming"],
                    "season": transfer["season"],
                    "marketValue": transfer["marketValue"],
                    "fee": fee,
                }

                result.append(transfer_record)
            except Exception as e:
                # Log the error and continue
                logging.error(f"Error processing transfer #{i} for player {self.player_id}: {str(e)}")
                continue

        return result

    def get_player_transfers(self) -> dict:
        """
        Retrieve and parse the transfer history and youth clubs of the specified player from Transfermarkt.

        Returns:
            dict: A dictionary containing the player's unique identifier, parsed transfer history, youth clubs,
                  and the timestamp of when the data was last updated.
        """
        self.response["id"] = self.player_id

        try:
            self.response["transfers"] = self.__parse_player_transfer_history()
        except Exception as e:
            logging.error(f"Failed to parse transfer history for player {self.player_id}: {str(e)}")
            self.response["transfers"] = []

        try:
            self.response["youthClubs"] = safe_split(self.get_text_by_xpath(Players.Transfers.YOUTH_CLUBS), ",")
        except Exception as e:
            logging.error(f"Failed to parse youth clubs for player {self.player_id}: {str(e)}")
            self.response["youthClubs"] = []

        return self.response