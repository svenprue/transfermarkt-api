from datetime import date
from enum import Enum
from typing import Optional

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, TransfermarktBaseModel


from datetime import date
from typing import Optional

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, TransfermarktBaseModel

class ManagerPlaceOfBirth(TransfermarktBaseModel):
    city: Optional[str]
    country: Optional[str]


class ManagerClub(TransfermarktBaseModel):
    id: str
    name: str
    role: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]


class PlayerProfile(TransfermarktBaseModel):
    id: str
    url: HttpUrl
    retired: bool
    retired_since: Optional[date]

class ManagerProfile(TransfermarktBaseModel, AuditMixin):
    id: str
    url: HttpUrl
    name: str
    full_name: Optional[str]
    image_url: Optional[HttpUrl]
    date_of_birth: Optional[date]
    place_of_birth: ManagerPlaceOfBirth
    age: Optional[int]
    citizenship: list[str]
    club: Optional[ManagerClub]
    player_profile: Optional[PlayerProfile]