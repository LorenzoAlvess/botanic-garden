from django.shortcuts import render
from garden.models import PlantLocation
import json

def plant_map(request):
    # Aqui, estou criando algumas localizações de plantas estáticas como exemplo
    static_plant_locations = [
        {'latitude': -18.675569, 'longitude': -39.862455, 'garden_name': 'Jardim Botânico', 'species_name': 'Rosa'},
        {'latitude': -18.675100, 'longitude': -39.862700, 'garden_name': 'Jardim Botânico', 'species_name': 'Orquídea'},
        {'latitude': -18.675800, 'longitude': -39.862200, 'garden_name': 'Jardim Botânico', 'species_name': 'Lírio'},
    ]
    # Convertendo os dados para JSON
    static_plant_data_json = json.dumps(static_plant_locations)
    return render(request, 'plant_map.html', {'plant_data_json': static_plant_data_json})


def index(request):
    return render(request, 'index.html')
