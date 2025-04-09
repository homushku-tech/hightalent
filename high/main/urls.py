from main.views import TableView, ReservationView
from django.urls import path

urlpatterns = [
    path('tables/', TableView.as_view(), name='table-list-create-destroy'),
    path('reservations/', ReservationView.as_view(), name='reservation-list-create-destroy'),
]
