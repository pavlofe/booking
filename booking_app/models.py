from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
            ('economy', 'Economy'),
            ('standard', 'Standard'),
            ('deluxe', 'Deluxe'),
            ('suite', 'Suite'),
        ]
    title = models.CharField(max_length=150)
    places = models.IntegerField(default=2)
    price = models.IntegerField(default=2500)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="room_images/")
    room_type = models.CharField(max_length=20,choices=ROOM_TYPES)

    def __str__(self):
        return self.title

class Booking(models.Model):
    STATUS_CHOICES = [
        ('wtn', 'Очікує підтвердження'),
        ('cnf', 'Підтверджено'),
        ('clc', 'Скасовано')
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    email = models.EmailField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.room.title} from {self.check_in_date} to {self.check_out_date} by {self.user.username}"
