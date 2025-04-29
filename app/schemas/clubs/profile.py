from datetime import date
from typing import Optional

from app.schemas.base import TransfermarktBaseModel


class ClubSquad(TransfermarktBaseModel):
    size: int
    average_age: float
    foreigners: int
    national_team_players: int


class ClubLeague(TransfermarktBaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    country_id: Optional[str] = None
    country_name: Optional[str] = None
    tier: Optional[str] = None


class ClubProfile(TransfermarktBaseModel):
    id: str
    url: str
    name: str
    official_name: Optional[str] = None
    image: str
    founded_on: Optional[date] = None
    current_market_value: Optional[int] = None
    confederation: Optional[str] = None
    isNational: bool
    fifa_world_ranking: Optional[str] = None
    league: ClubLeague
