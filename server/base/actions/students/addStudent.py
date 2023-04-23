from fastapi.encoders import jsonable_encoder

from bson.objectid import ObjectId

from server.base.models.StudentModel import StudentModel

from server.base.connect import db


async def add_student(student: StudentModel):
    existedMail = await db["Students"].find_one({"email": student.email})

    if existedMail is not None:
        return "email already in use"

    student.id = ObjectId()

    student_dict = jsonable_encoder(student)

    await db["Students"].insert_one(student_dict)

    return "Created"
