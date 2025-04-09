import pytest
from rest_framework.test import APIClient
from rest_framework import status
from main.models import Table, Reservation
from django.utils.timezone import now, timedelta

# Фикстура для создания экземпляра API-клиента.
@pytest.fixture
def api_client():
    return APIClient()

# Фикстура для создания тестовой стола.
@pytest.fixture
def create_table():
    return Table.objects.create(name="Table 1", seats=4, location="Near window")

# Фикстура для создания тестовой брони.
@pytest.fixture
def create_reservation(create_table):
    return Reservation.objects.create(
        customer_name="John Doe",
        table=create_table,
        reservation_date=now(),
        duration_minutes=60
    )
# Тест на создание нового стола через API.
@pytest.mark.django_db # Указывает, что тест использует базу данных.
def test_create_table(api_client):
    payload = {
        "name": "Table 2",
        "seats": 6,
        "location": "Center"
    }
    response = api_client.post("/api/tables/", payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Table.objects.filter(name="Table 2").exists()

@pytest.mark.django_db
def test_list_tables(api_client, create_table):
    response = api_client.get("/api/tables/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Table 1"

@pytest.mark.django_db
def test_create_reservation(api_client, create_table):
    payload = {
        "customer_name": "Jane Doe",
        "table": create_table.id,
        "reservation_date": now().isoformat(),
        "duration_minutes": 90
    }
    response = api_client.post("/api/reservations/", payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Reservation.objects.filter(customer_name="Jane Doe").exists()

@pytest.mark.django_db
def test_reservation_conflict(api_client, create_reservation):
    payload = {
        "customer_name": "Jane Doe",
        "table": create_reservation.table.id,
        "reservation_date": create_reservation.reservation_date.isoformat(),
        "duration_minutes": 30
    }
    response = api_client.post("/api/reservations/", payload, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Этот столик уже зарезервирован на указанное время." in str(response.data)