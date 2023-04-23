from bson import ObjectId
from pydantic import BaseModel, Field

from server.base.models.PyObjectID import PyObjectID


class TeacherModel(BaseModel):
    id: PyObjectID = Field(default_factory=PyObjectID, alias="_id")
    email: str = Field(...)
    password: str = Field(...)
    name: str = Field(...)
    fieldOfSport: str = Field(...)
    experience: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
