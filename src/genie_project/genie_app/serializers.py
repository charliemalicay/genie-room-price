from rest_framework import serializers
from .models import HotelRoom


class EventsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return HotelRoom.objects.create(**validated_data)

    class Meta:
        model = HotelRoom
        fields = ['id', 'room_id', 'night_of_stay', 'rpg_status', 'timestamp', 'hotel_id']


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = ['hotel_id', 'timestamp']
