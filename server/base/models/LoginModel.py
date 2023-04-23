from pydantic import BaseModel, Field

from server.base.models import PyObjectID


class LoginModel(BaseModel):
    id: PyObjectID = Field(default_factory=PyObjectID, alias="_id")
    email: Field(...)
    password: Field(...)
