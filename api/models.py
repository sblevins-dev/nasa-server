from django.db import models

# Create your models here.
class PictureOfDay(models.Model):
    date = models.DateField()
    explanation = models.TextField()
    hdurl = models.URLField()
    media_type = models.CharField(max_length=50)
    service_version = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title