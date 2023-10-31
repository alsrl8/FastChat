from typing import Annotated

from bson import ObjectId
from pydantic import BaseModel

from database.models.object import ObjectIdPydanticAnnotation


class User(BaseModel):
    _id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = None
    name: str = ''
    google_email: str = ''
