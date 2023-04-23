from fastapi import APIRouter, Body, responses, HTTPException
from server.base.actions.students.addStudent import add_student

from server.base.models.StudentModel import StudentModel


router = APIRouter(
    prefix="/students",
    tags=["students"]
)


@router.post("/add")
async def addStudent(user: StudentModel = Body(...)):
    res = await add_student(user)
    if res == "Created":
        return responses.JSONResponse(status_code=202, content={"message": res})
    else:
        raise HTTPException(status_code=409, detail={"message": res})
