from django.urls import path
from . import views

urlpatterns = [
    # path("daypic/", views.PictureOfDayCreate.as_view(), name="daypic-create"),
    path('daypic/', views.PictureOfDay.as_view(), name="get-picture-of-day"),
    path('roverPhotos/', views.RoverPhotos.as_view(), name="rover-photos")
]