from django.urls import path,include
from .views import *

urlpatterns = [
    path('roomlist/',GetRoomAPI.as_view(),name='list-room'),
]
