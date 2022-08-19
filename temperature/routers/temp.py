from fastapi import APIRouter
from repo import temp

router = APIRouter(
    prefix="/temperature",
    tags=["Temperature"]
)


@router.get("/")
def all_items():
    return temp.all_temp()


@router.post("/")
def add_temp(new):
    return temp.add_temp(new)


@router.get("/latest")
def latest_temp():
    return temp.latest_temp()
