from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    picture = models.ImageField(upload_to ='Pictures',  default = 'pictures/None/SampleImg.jpg')
    def __str__(self):
        return self.name