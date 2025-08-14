from django.shortcuts import render
from booking_app.models import Room, Bookings

# Create your views here.
def home(request):
    rooms = Room.object.all()
    return render(request, context={'rooms':rooms})