from django.db import models

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

