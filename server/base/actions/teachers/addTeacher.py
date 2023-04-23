from fastapi.encoders import jsonable_encoder

from bson.objectid import ObjectId

from server.base.models.TeacherModel import TeacherModel

from server.base.connect import db


async def add_teacher(teacher: TeacherModel):
    existedMail = await db["Teachers"].find_one({"email": teacher.email})

    if existedMail is not None:
        return "email already in use"

    teacher.id = ObjectId()

    teacher_dict = jsonable_encoder(teacher)

    await db["Teachers"].insert_one(teacher_dict)

    return "Created"
