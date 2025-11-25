from pydantic import BaseModel, ConfigDict
from typing import Optional


class OperatorCreate(BaseModel):
    name: str
    alive: bool = True
    limit: int = 10


class OperatorUpdate(BaseModel):
    alive: Optional[bool] = None
    limit: Optional[int] = None


class OperatorOut(BaseModel):
    id: int
    name: str
    alive: bool
    limit: int
    active_contacts: int

    model_config = ConfigDict(from_attributes=True)