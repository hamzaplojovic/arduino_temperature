from fastapi import APIRouter
from repo import humidity

router = APIRouter(
    prefix="/humidity",
    tags=["humidity"]
)


@router.get("/")
def all_items():
    return humidity.all_items()


@router.get("/latest")
def latest():
    return humidity.latest_humidity()


@router.post("/")
def add(new):
    return humidity.add_humidity(new)
