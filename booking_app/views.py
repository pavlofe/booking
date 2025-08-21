from django.shortcuts import render
from booking_app.models import Room, Booking
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    rooms = Room.objects.all()
    return render(request,"index.html", context={'rooms':rooms})

def room_page(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'room-info.html', context={'room':room})