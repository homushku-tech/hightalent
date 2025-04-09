from .models import Table, Reservation
from main.serializer import TableSerializers, ReservationSerializers
from rest_framework import generics


class TableView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializers


class ReservationView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers


