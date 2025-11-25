from fastapi import APIRouter, HTTPException
from database import OperatorTable
from ..schemas import OperatorCreate, OperatorUpdate, OperatorOut

router = APIRouter(prefix="/operators", tags=["operators"])


@router.post("", response_model=OperatorOut)
def create_operator(data: OperatorCreate):
    return OperatorTable.insert(name=data.name, alive=data.alive, limit=data.limit)


@router.get("")
def list_operators():
    return OperatorTable.get_row_all()


@router.patch("/{operator_id}")
def update_operator(operator_id: int, data: OperatorUpdate):
    operator = OperatorTable.get_row(operator_id=operator_id)
    if not operator:
        raise HTTPException(404, "Operator not found")

    if data.alive is not None:
        OperatorTable.update(operator_id=operator_id, key="alive", value=data.alive)
    if data.limit is not None:
        OperatorTable.update(operator_id=operator_id, key="limit", value=data.limit)

    return OperatorTable.get_row(operator_id=operator_id)
