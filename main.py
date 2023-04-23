from fastapi import FastAPI
from fastapi.responses import JSONResponse
import server.base.connect

mainRouter = FastAPI()


@mainRouter.get("/")
async def main():
    return JSONResponse(status_code=200, content={"message": "Work"})
