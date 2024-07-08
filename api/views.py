from rest_framework import generics, status
from .models import PictureOfDay
from .serializers import PictureOfDaySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
import requests

# Create your views here.
# class PictureOfDayCreate(generics.CreateAPIView):
#     queryset = PictureOfDay.objects.all()
#     serializer_class = PictureOfDaySerializer

class PictureOfDay(APIView):
    def get(self, request, *args, **kwargs):
        api_key = config('API_KEY')
        url = config('DAY_PIC_URL')
        params = {'api_key': api_key}

        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return Response(data)
        else:
            return Response({'error': 'Failed to retrieve data'}, status=response.status_code)
        
class RoverPhotos(APIView):
    def get(self, request, *args, **kwargs):
        url = config('ROVER_URL')

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return Response(data)
        else:
            return Response({'error': 'Failed to retrieve data'}, status=response.status_code)
