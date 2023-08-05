from enum import Enum
from pydantic import BaseModel


class ModelLanguage(str, Enum):
    en = "en"


class ModelSize(str, Enum):
    sm = "sm"


class UserRequestIn(BaseModel):
    text: str
    model_language: ModelLanguage = "en"
    model_size: ModelSize = "sm"
