from django.urls import path
from .views import home, room_page
urlpatterns = [
    path('', home, name='home'),
    path('room/<int:room_id>',room_page, name='room_info'),

]
