from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict


class ContactCreate(BaseModel):
    external_id: str
    source_id: int
    payload: Optional[Dict] = None


class ContactOut(BaseModel):
    id: int
    lead_id: int
    source_id: int
    operator_id: int | None
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
