from fastapi import APIRouter, Body, responses, HTTPException
from server.base.actions.loginValidate import login_validate
from server.base.models.LoginModel import LoginModel


router = APIRouter(
    prefix="/login",
    tags=["login"]
)


@router.post("/")
async def login(user: LoginModel = Body(...)):
    res = await login_validate(user)
    if res == "Accepted":
        return responses.JSONResponse(status_code=201, content={"message": res})
    else:
        raise HTTPException(status_code=409, detail={"message": res})
