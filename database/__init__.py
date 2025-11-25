from .leads import LeadTable
from .sources import SourceTable
from .weights import SOWTable
from .contacts import ContactsTable
from .operators import OperatorTable
from .db import engine, Base

Base.metadata.create_all(engine)

__all__ = {"LeadTable", "SourceTable", "SOWTable", "ContactsTable", "OperatorTable"}
