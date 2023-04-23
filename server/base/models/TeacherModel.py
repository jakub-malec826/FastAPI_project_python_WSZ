from pydantic import BaseModel, Field

from server.base.models import PyObjectID


class TeacherModel(BaseModel):
    id: PyObjectID = Field(default_factory=PyObjectID, alias="_id")
    email: Field(...)
    password: Field(...)
    name: Field(...)
    fieldOfSport: Field(...)
    experience: Field(...)