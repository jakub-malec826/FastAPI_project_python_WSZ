from server.base.models.LoginModel import LoginModel

from server.base.connect import db


async def login_validate(login: LoginModel):
    existUser = await db[login.typeOfUser].find_one({"email": login.email})

    if not existUser:
        return "User not found"

    if existUser["password"] != login.password:
        return "Password incorrect"

    return "Accepted"  