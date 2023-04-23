from fastapi.encoders import jsonable_encoder

from bson.objectid import ObjectId

from ..models.StudentModel import StudentModel

from ..connect import db


async def add_student(student: StudentModel):
    existedMail = await db["Teachers"].find_one({"email": student.email})
    existedUserName = await db["Teachers"].find_one({"username": student.username})

    if existedMail is not None:
        return "email already in use"

    if existedUserName is not None:
        return "username already in use"

    student.id = ObjectId()

    student_dict = jsonable_encoder(student)

    await db["Teachers"].insert_one(student_dict)

    return "Created"
