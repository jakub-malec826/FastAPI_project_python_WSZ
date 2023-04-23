from fastapi import APIRouter, Body, responses, HTTPException
from server.base.actions.teachers.addTeacher import add_teacher
from server.base.actions.teachers.showTeachers import show_teachers

from server.base.models.TeacherModel import TeacherModel


router = APIRouter(
    prefix="/teachers",
    tags=["teachers"]
)


@router.get("/")
async def showTeachers():
    res = await show_teachers()
    return responses.JSONResponse(status_code=200, content=res)


@router.post("/add")
async def addTeacher(user: TeacherModel = Body(...)):
    res = await add_teacher(user)
    if res == "Created":
        return responses.JSONResponse(status_code=202, content={"message": res})
    else:
        raise HTTPException(status_code=409, detail={"message": res})
