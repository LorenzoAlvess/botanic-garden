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
    cod = models.CharField(max_length=255, unique=True)
    garden = models.ForeignKey('Garden', on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    condition = models.CharField(max_length=255, blank=True, help_text="Condition of the plant at the location.")
    notes = models.TextField(blank=True, help_text="Additional notes about the plant's location.")
    image_url = models.URLField(blank=True, help_text="URL to an image of the plant at this location.")
    exsicata_image_url = models.URLField(blank=True, help_text="URL to the digitalized image of the exsicata.")
    qr_code_url = models.URLField(blank=True, help_text="URL to the QR code image or data.")

    def __str__(self):
        return f"{self.garden.name} - {self.species.name}"

