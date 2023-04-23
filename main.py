from fastapi import FastAPI
from fastapi.responses import JSONResponse
from server.routers import login, students, teachers

import server.base.connect


mainRouter = FastAPI()


mainRouter.include_router(login.router)
mainRouter.include_router(students.router)
mainRouter.include_router(teachers.router)


@mainRouter.get("/")
async def main():
    return JSONResponse(status_code=200, content={"message": "Work"})
