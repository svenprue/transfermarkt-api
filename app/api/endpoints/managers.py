from typing import Optional

from fastapi import APIRouter

from app.schemas import managers as schemas
from app.services.managers.profile import TransfermarktManagerProfile
from app.services.managers.contracts import TransfermarktManagerContracts

router = APIRouter()

@router.get("/profile/{manager_id}", response_model=schemas.ManagerProfile)
def get_manager_profile(manager_id: str):
    tfmkt = TransfermarktManagerProfile(manager_id=manager_id)
    manager_profiles = tfmkt.get_manager_profile()
    return manager_profiles

@router.get("/contracts/{manager_id}", response_model=schemas.ManagerContracts)
def get_manager_contracts(manager_id: str):
    tfmkt = TransfermarktManagerContracts(manager_id=manager_id)
    manager_contracts = tfmkt.get_manager_contracts()
    return manager_contracts
