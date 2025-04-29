from datetime import date
from typing import Optional

from app.schemas.base import AuditMixin, TransfermarktBaseModel


class ClubManager(TransfermarktBaseModel):
    id: str
    name: str
    nationality: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    time_in_office: Optional[int] = None
    games: Optional[int] = None
    points_per_game: Optional[float] = None


class ClubManagers(TransfermarktBaseModel, AuditMixin):
    id: str
    managers: list[ClubManager]
