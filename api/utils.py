import random
from database import SOWTable, OperatorTable


def choose_operator(source_id: int):
    weights = SOWTable.get_row_by_id_all(source_id=source_id)

    candidates = []
    for item in weights:
        operator = OperatorTable.get_row(operator_id=item.operator_id)
        if operator is not None and operator.alive and operator.active_contacts < operator.limit and item.weight > 0:
            candidates.append((operator, item.weight))

    if not candidates:
        return None

    total = sum(weight for _, weight in candidates)
    rand = random.uniform(0, total)
    upto = 0
    print(f"{candidates=}")
    for operator, weight in candidates:
        upto += weight
        if rand <= upto:
            return operator
    return candidates[-1][0]
