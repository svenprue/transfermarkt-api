from datetime import date
from typing import Optional, List

from app.schemas.base import AuditMixin, TransfermarktBaseModel


class PlayerTransferClub(TransfermarktBaseModel):
    id: str
    name: str


class PlayerTransfer(TransfermarktBaseModel):
    id: str
    club_from: PlayerTransferClub
    club_to: PlayerTransferClub
    date: Optional[date]
    upcoming: Optional[bool] 
    season: Optional[str] 
    market_value: Optional[int] 
    fee: Optional[int] 


class PlayerTransfers(TransfermarktBaseModel, AuditMixin):
    id: str
    transfers: List[PlayerTransfer]
    youth_clubs: Optional[List[str]] 