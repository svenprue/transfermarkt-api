from datetime import date
from typing import Optional

from app.schemas.base import AuditMixin, TransfermarktBaseModel


class ManagerContractsClub(TransfermarktBaseModel):
    id: str
    name: str


class ManagerContract(TransfermarktBaseModel):
    id: str
    club: ManagerContractsClub
    role: str
    start_date: date
    end_date: date

class ManagerContracts(TransfermarktBaseModel, AuditMixin):
    id: str
    contracts: list[ManagerContract]
