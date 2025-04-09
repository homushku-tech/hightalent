from django.db import models

class Table(models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField()
    location = models.TextField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    duration_minutes = models.IntegerField() 

    def __str__(self):
        return f"{self.customer_name} - {self.table.name} - {self.reservation_date}"