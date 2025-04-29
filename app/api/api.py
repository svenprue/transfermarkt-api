from fastapi import APIRouter

from app.api.endpoints import clubs, competitions, players, managers

api_router = APIRouter()
api_router.include_router(competitions.router, prefix="/competitions", tags=["competitions"])
api_router.include_router(clubs.router, prefix="/clubs", tags=["clubs"])
api_router.include_router(players.router, prefix="/players", tags=["players"])

api_router.include_router(managers.router, prefix="/managers", tags=["managers"])
