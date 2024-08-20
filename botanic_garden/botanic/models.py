from django.db import models


class Family(models.Model):
    """
    Represents a botanical family.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the family.")
    description = models.TextField(blank=True, help_text="Description of the family.")

    def __str__(self):
        return self.name


class Genus(models.Model):
    """
    Represents a botanical genus.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the genus.")
    family = models.ForeignKey(Family, on_delete=models.CASCADE, help_text="Family to which the genus belongs.")
    description = models.TextField(blank=True, help_text="Description of the genus.")

    def __str__(self):
        return self.name


class Species(models.Model):
    """
    Represents a botanical species.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the species.")
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE, help_text="Genus to which the species belongs.")
    description = models.TextField(blank=True, help_text="Description of the species.")
    blooming_season = models.CharField(max_length=50, blank=True, help_text="Blooming season of the species.")
    average_height = models.FloatField(null=True, blank=True, help_text="Average height of the species.")
    image_url = models.URLField(blank=True, help_text="URL of the representative image of the species.")
    collections = models.ManyToManyField('Collection', blank=True, help_text="Collections to which the species belongs.")

    def __str__(self):
        return self.name


class Collection(models.Model):
    """
    Represents a botanical collection.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the collection.")
    description = models.TextField(blank=True, help_text="Description of the collection.")

    def __str__(self):
        return self.name
