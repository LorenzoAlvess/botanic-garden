from django.shortcuts import render
from garden.models import PlantLocation
from django.http import JsonResponse
from botanic.models import Family, Genus, Species
import json

def plant_map(request):
    # Recuperar parâmetros de filtro
    family_id = request.GET.get('family')
    genus_id = request.GET.get('genus')
    species_id = request.GET.get('species')

    # Recuperar dados do modelo PlantLocation com base nos filtros
    plant_locations = PlantLocation.objects.all()

    if family_id:
        plant_locations = plant_locations.filter(species__genus__family__id=family_id)
    if genus_id:
        plant_locations = plant_locations.filter(species__genus__id=genus_id)
    if species_id:
        plant_locations = plant_locations.filter(species__id=species_id)

    # Preparar os dados para o JSON
    plant_data = []
    for location in plant_locations:
        plant_data.append({
            'latitude': location.latitude,
            'longitude': location.longitude,
            'garden_name': location.garden.name,
            'species_name': location.species.name
        })

    # Convertendo os dados para JSON
    plant_data_json = json.dumps(plant_data)

    # Dados para os filtros, ordenados alfabeticamente
    families = Family.objects.all().order_by('name')
    genera = Genus.objects.all().order_by('name')
    species_list = Species.objects.all().order_by('name')

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'plant_data': plant_data})
    
    return render(request, 'plant_map.html', {
        'plant_data_json': plant_data_json,
        'families': families,
        'genera': genera,
        'species_list': species_list
    })




def index(request):
    return render(request, 'index.html')
