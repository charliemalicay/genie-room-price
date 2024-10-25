from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from .models import HotelRoom
from .paginations import EventsLimitOffsetPagination
from .serializers import EventsSerializer, DashboardSerializer


class GetHotelRoomList(generics.ListCreateAPIView):
    serializer_class = EventsSerializer
    permission_classes = []
    pagination_class = EventsLimitOffsetPagination

    def get_queryset(self):
        # region Initialize params query
        param_hotel_id = self.request.GET.get('hotel_id')
        param_rpg_status = self.request.GET.get('rpg_status')
        param_room_id = self.request.GET.get('room_id')
        param_updated_gte = self.request.GET.get('updated__gte')
        param_updated_lte = self.request.GET.get('updated__lte')
        param_night_of_stay_gte = self.request.GET.get('night_of_stay__gte')
        param_night_of_stay_lte = self.request.GET.get('night_of_stay__lte')
        # endregion

        # region Building Params Data
        params = {}

        if param_hotel_id:
            params['hotel_id'] = int(param_hotel_id)

        if param_rpg_status:
            params['rpg_status'] = int(param_rpg_status)

        if param_room_id:
            params['room_id'] = param_room_id

        if param_updated_gte:
            params['timestamp__gte'] = param_updated_gte

        if param_updated_lte:
            params['timestamp__lte'] = param_updated_lte

        if param_night_of_stay_gte:
            params['night_of_stay__gte'] = param_night_of_stay_gte

        if param_night_of_stay_lte:
            params['night_of_stay__lte'] = param_night_of_stay_lte

        if params != {}:
            return HotelRoom.objects.filter(**params)
        # endregion

        return HotelRoom.objects.all()

    def post(self, request, format=None):
        serializer = EventsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetDashboardData(generics.ListCreateAPIView):
    serializer_class = DashboardSerializer
    permission_classes = []
    pagination_class = EventsLimitOffsetPagination

    def get_queryset(self):
        # region Initialize params query
        param_hotel_id = self.request.GET.get('hotel_id')
        param_period_month = self.request.GET.get('period_month')
        param_period_day = self.request.GET.get('period_day')
        param_period_year = self.request.GET.get('period_year')
        # endregion

        # region Building Params Data
        params = {}

        if param_hotel_id:
            params['hotel_id'] = int(param_hotel_id)

        if param_period_month:
            params['timestamp__month'] = int(param_period_month)

        if param_period_day:
            params['timestamp__day'] = int(param_period_day)

        if param_period_year:
            params['timestamp__year'] = int(param_period_year)

        if params != {}:
            return HotelRoom.objects.filter(**params).order_by('timestamp')
        # endregion

        return HotelRoom.objects.all().order_by('timestamp')
