from fastapi import APIRouter

from helper.cards import cards_router

router = APIRouter(prefix="/api")
router.include_router(cards_router)
