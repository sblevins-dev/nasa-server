from rest_framework import serializers
from .models import PictureOfDay

class PictureOfDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureOfDay
        fields = '__all__'

