from fastapi import FastAPI
from routers import temp, humidity


app = FastAPI()

app.include_router(temp.router)
app.include_router(humidity.router)
