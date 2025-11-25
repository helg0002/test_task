from fastapi import APIRouter, HTTPException
from database import SourceTable, SOWTable
from ..schemas import SourceCreate, WeightsCreate

router = APIRouter(prefix="/sources", tags=["sources"])


@router.post("")
def create_source(data: SourceCreate):
    return SourceTable.insert(name=data.name)


@router.get("")
def list_sources():
    return SourceTable.get_row_all()


@router.post("/{source_id}/weights")
def set_weights(source_id: int, payload: dict):
    source = SourceTable.get_row(source_id=source_id)
    if not source:
        raise HTTPException(404, "Source not found")

    items = payload.get("items", [])
    print(f"{items=}")
    if not items:
        raise HTTPException(400, "No weights provided")

    SOWTable.delete(source_id=source_id)

    for item in items:
        operator_id = item.get("operator_id")
        weight = item.get("weight")
        if operator_id is None or weight is None:
            continue
        SOWTable.insert(source_id=source_id, operator_id=operator_id, weight=weight)
    for i in SOWTable.get_row_by_id_all(source_id=source_id):
        print(f"{i.operator_id=}")
        print([{"operator_id": sow.operator_id, "weight": sow.weight}
            for sow in SOWTable.get_row_by_id_all(source_id=source_id)])
    return [{"operator_id": sow.operator_id, "weight": sow.weight}
            for sow in SOWTable.get_row_by_id_all(source_id=source_id)]
