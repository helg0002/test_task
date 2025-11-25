from pydantic import BaseModel
from typing import List


class SourceCreate(BaseModel):
    name: str


class WeightItem(BaseModel):
    operator_id: int
    weight: int


class WeightsCreate(BaseModel):
    items: List[WeightItem]

