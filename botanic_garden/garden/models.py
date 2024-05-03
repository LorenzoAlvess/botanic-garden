from django.db import models
from botanic.models import Species


class Garden(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    plants = models.ManyToManyField(Species, through='PlantLocation')

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    garden = models.ManyToManyField(Garden)

    def __str__(self):
        return self.name

class PlantLocation(models.Model):
    cod = models.CharField(max_length=255)
    garden = models.ForeignKey('Garden', on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.garden.name} - {self.species.name}"


