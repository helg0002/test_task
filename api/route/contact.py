from fastapi import APIRouter, HTTPException
from ..utils import choose_operator
from ..schemas import ContactCreate, ContactOut
from database import (
    LeadTable,
    SourceTable,
    ContactsTable,
    OperatorTable
)

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("")
def create_contact(data: ContactCreate):
    lead = LeadTable.get_row(external_id=data.external_id)
    if not lead:
        lead = LeadTable.insert(external_id=data.external_id)

    source = SourceTable.get_row(source_id=data.source_id)
    if not source:
        raise HTTPException(404, "Source not found")

    operator = choose_operator(source_id=source.id)
    print(f"{operator}")
    contact = ContactsTable.insert(lead_id=lead.id, source_id=source.id, operator_id=(operator.id if operator else None))

    if operator:
        operator = OperatorTable.increment_active_contacts(operator_id=operator.id)

    return {
        "contact_id": contact.id,
        "lead_id": lead.id,
        "source_id": source.id,
        "operator_id": contact.operator_id,
        "assigned": operator is not None
    }
