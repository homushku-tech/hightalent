from rest_framework import serializers
from main.models import Table, Reservation

from datetime import timedelta

class TableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Table 
        fields = '__all__'  


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'  

    def validate(self, data):
        table = data['table']
        reservation_date = data['reservation_date']
        duration = data['duration_minutes']
        end_time = reservation_date + timedelta(hours=duration)
        flag_reservations = Reservation.objects.filter(
            table=table,
            reservation_date__lt=end_time,
            reservation_date__gte=reservation_date
        )
        if flag_reservations.exists():
            raise serializers.ValidationError("Этот столик уже зарезервирован на указанное время.")
        return data