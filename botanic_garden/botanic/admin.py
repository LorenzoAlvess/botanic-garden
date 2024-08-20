from django.contrib import admin
from .models import Family, Genus, Species, Collection

class SpeciesAdmin(admin.ModelAdmin):
    search_fields = ['name']  # Define which fields should be searchable

admin.site.register(Family)
admin.site.register(Genus)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Collection)
