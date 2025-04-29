from dataclasses import dataclass
import re

from app.services.base import TransfermarktBase
from app.utils.utils import extract_from_url
from app.utils.xpath import Managers


@dataclass
class TransfermarktManagerContracts(TransfermarktBase):
    """
    Retrieves and parses a manager's transfer history from Transfermarkt.
    """

    manager_id: str = None
    URL: str = "https://www.transfermarkt.com/-/stationen/trainer/{manager_id}"

    def __post_init__(self) -> None:
        """Initialize the TransfermarktManagerTransfers class."""
        self.URL = self.URL.format(manager_id=self.manager_id)
        self.page = self.request_url_page()

    def __parse_manager_transfer_history(self) -> list:
        """Parses the manager's history table and extracts transfer details."""

        table = self.page.xpath(Managers.Contracts.TABLE)
        if not table:
            return []

        rows = table[0].xpath(Managers.Contracts.ROWS)
        contracts = []

        for row in rows:
            try:
                # Get club link and extract club ID directly from URL
                club_link = row.xpath(Managers.Contracts.CLUB_LINK)
                if not club_link:
                    continue

                club_link = club_link[0]
                club_id = club_link.split("/")[-1]  # Extract ID from the last part of URL

                # Get club name and role
                club_name = row.xpath(Managers.Contracts.CLUB_NAME)
                club_name = club_name[0].strip() if club_name else ""

                role = row.xpath(Managers.Contracts.ROLE)
                role = role[0].strip() if role else ""

                # Process start date - extract date in parentheses if available
                start_date = row.xpath(Managers.Contracts.START_DATE)
                if start_date:
                    start_date_raw = start_date[0].strip()
                    start_date_match = re.search(r"\((.*?)\)", start_date_raw)
                    start_date_str = start_date_match.group(1) if start_date_match else start_date_raw
                else:
                    start_date_str = ""

                # Process end date - extract date in parentheses or remove "expected" text
                end_date = row.xpath(Managers.Contracts.END_DATE)
                print(end_date)
                if end_date:
                    end_date_raw = end_date[0].strip()
                    # Check for expected date format like "expected Jun 30, 2026"
                    expected_match = re.search(r"expected\s+(.*?)$", end_date_raw)
                    if expected_match:
                        end_date_str = expected_match.group(1).strip()
                    else:
                        # Handle regular date format (possibly with parentheses)
                        end_date_match = re.search(r"\((.*?)\)", end_date_raw)
                        end_date_str = end_date_match.group(1) if end_date_match else end_date_raw
                else:
                    end_date_str = ""

                contracts.append(
                    {
                        "id": self.manager_id,
                        "club": {
                            "id": club_id,
                            "name": club_name,
                        },
                        "role": role,
                        "startDate": start_date_str,
                        "endDate": end_date_str,
                    }
                )
            except Exception as e:
                print(f"Error parsing row: {e}")
                continue

        return contracts

    def get_manager_contracts(self) -> dict:
        """Retrieves and parses manager transfer history."""
        self.response["id"] = self.manager_id
        self.response["contracts"] = self.__parse_manager_transfer_history()
        return self.response
