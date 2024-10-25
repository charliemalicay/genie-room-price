from django.urls import path
from .views import GetHotelRoomList, GetDashboardData


urlpatterns = [
    path('events/', GetHotelRoomList.as_view(), name='get-hotel-room-list'),
    path('dashboard/', GetDashboardData.as_view(), name='get-hotel-room-dashboard'),
]
