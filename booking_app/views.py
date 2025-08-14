from django.shortcuts import render
from booking_app.models import Room, Booking
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    rooms = Room.objects.all()
    return render(request,"index.html", context={'rooms':rooms})
