from fastapi.encoders import jsonable_encoder

from bson.objectid import ObjectId

from ..models.TeacherModel import TeacherModel

from ..connect import db


async def add_teacher(teacher: TeacherModel):
    existedMail = await db["Teachers"].find_one({"email": teacher.email})
    existedUserName = await db["Teachers"].find_one({"username": teacher.username})

    if existedMail is not None:
        return "email already in use"

    if existedUserName is not None:
        return "username already in use"

    teacher.id = ObjectId()

    teacher_dict = jsonable_encoder(teacher)

    await db["Teachers"].insert_one(teacher_dict)

    return "Created"
