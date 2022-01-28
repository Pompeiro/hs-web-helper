import typing as T

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from helper.dependencies import get_db

from . import crud, models, schemas

router = APIRouter(prefix="/cards", tags=["cards"])


@router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)) -> models.Item:
    return crud.create_item(db=db, item=item)


@router.get("/items", response_model=T.List[schemas.Item])
def read_items(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> T.List[models.Item]:
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
