from datetime import datetime
from unittest.mock import patch

import pytest
from fastapi import HTTPException
from schema import And, Or, Schema

from app.services.clubs.managers import TransfermarktClubManagers


def test_get_club_managers_not_found():
    with pytest.raises(HTTPException):
        TransfermarktClubManagers(club_id="0").get_club_managers()


@pytest.mark.parametrize("club_id", ["418", "131", "210"])  # Example club IDs
@patch("app.utils.utils.clean_response", side_effect=lambda x: x)
def test_get_club_managers(
        mock_get,
        club_id,
        regex_date_dd_mm_yyyy,
        regex_float_or_int,
        len_greater_than_0,
):
    tfmkt = TransfermarktClubManagers(club_id=club_id)
    result = tfmkt.get_club_managers()

    expected_schema = Schema(
        {
            "id": And(str, len_greater_than_0),
            "managers": [
                {
                    "id": And(str, len_greater_than_0),
                    "name": And(str, len_greater_than_0),
                    "nationality": And(str),
                    "start_date": And(str, regex_date_dd_mm_yyyy),  # Assuming dd.mm.yyyy format
                    "end_date": Or(None, And(str, regex_date_dd_mm_yyyy)),
                    "time_in_office": And(str),
                    "games": And(str),  # Could be an empty string if no games
                    "points_per_game": Or(None, And(str, regex_float_or_int)),  # or empty string.
                },
            ],
        },
    )

    assert expected_schema.validate(result)
