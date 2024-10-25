from django.db import models


class HotelRoom(models.Model):
    RPG_STATUS_CHOICES = (
        ('1', 'booking'),
        ('2', 'cancellation'),
    )

    id = models.AutoField(primary_key=True)
    room_id = models.CharField(max_length=500)
    night_of_stay = models.DateField()
    rpg_status = models.CharField(max_length=1, choices=RPG_STATUS_CHOICES)
    timestamp = models.DateTimeField()
    hotel_id = models.IntegerField()

    def __str__(self):
        return f"id: {id} - Hotel ID: {hotel_id}"

    class Meta:
        db_table = "HotelRoom"
