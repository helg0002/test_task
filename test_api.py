import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_operator():
    response = client.post("/operators", json={
        "name": "Operator A",
        "alive": True,
        "limit": 2
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Operator A"
    assert data["limit"] == 2


def test_create_source():
    response = client.post("/sources", json={"name": "Bot A"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bot A"


def test_set_weights():
    sources = client.get("/sources").json()
    operators = client.get("/operators").json()
    source_id = sources[0]["id"]
    operator_id = operators[0]["id"]

    response = client.post(f"/sources/{source_id}/weights", json={
        "items": [{"operator_id": operator_id, "weight": 100}]
    })
    assert response.status_code == 200
    weights = response.json()
    assert weights[0]["weight"] == 100


# def test_create_contact_and_assign_operator():
#     sources = client.get("/sources").json()
#     source_id = sources[0]["id"]
#
#     response = client.post("/contacts", json={
#         "external_id": "lead_123",
#         "source_id": source_id
#     })
#     assert response.status_code == 200
#     data = response.json()
#     assert "contact_id" in data
#     assert "lead_id" in data
#     assert data["assigned"] is True


def test_operator_limit_respected():
    sources = client.get("/sources").json()
    source_id = sources[0]["id"]

    for i in range(3):
        response = client.post("/contacts", json={
            "external_id": f"lead_limit_{i}",
            "source_id": source_id
        })
        assert response.status_code == 200
        data = response.json()
        print(f"{data=}")
        if i < 2:
            assert data["assigned"] is True
        else:
            assert data["assigned"] is False
