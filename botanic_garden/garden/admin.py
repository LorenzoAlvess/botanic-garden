from django.contrib import admin
from .models import Event, PlantLocation, Garden
from botanic.models import Species

class PlantLocationAdmin(admin.ModelAdmin):
    list_display = ('cod', 'garden', 'species', 'latitude', 'longitude', 'condition')
    autocomplete_fields = ('species',)  # Enable autocomplete for species
    search_fields = ('species__name', 'garden__name', 'notes')  # Ensure these fields exist and are searchable
    list_filter = ('garden', 'species')
    list_per_page = 20

admin.site.register(Event)
admin.site.register(Garden)
admin.site.register(PlantLocation, PlantLocationAdmin)
