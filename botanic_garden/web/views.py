from django.shortcuts import render
from garden.models import PlantLocation
import random
import json

def plant_map(request):
    # Exemplo de dados estáticos
    static_plant_locations = [
        {'latitude': -18.675569, 'longitude': -39.862455, 'garden_name': 'Jardim Botânico', 'species_name': 'Rosa'},
        {'latitude': -18.675100, 'longitude': -39.862700, 'garden_name': 'Jardim Botânico', 'species_name': 'Orquídea'},
        {'latitude': -18.675800, 'longitude': -39.862200, 'garden_name': 'Jardim Botânico', 'species_name': 'Lírio'},
    ]
    
    # Gerar novas localizações aleatórias para alcançar pelo menos 10
    num_new_locations = 10 - len(static_plant_locations)
    for _ in range(num_new_locations):
        # Simulação de novas localizações próximas
        lat = random.uniform(-18.676, -18.674)
        lng = random.uniform(-39.863, -39.861)
        plant_name = random.choice(['Girassol', 'Tulipa', 'Cacto', 'Bromélia', 'Hortênsia'])
        static_plant_locations.append({
            'latitude': lat,
            'longitude': lng,
            'garden_name': 'Jardim Botânico',
            'species_name': plant_name
        })

    # Convertendo os dados para JSON
    static_plant_data_json = json.dumps(static_plant_locations)
    return render(request, 'plant_map.html', {'plant_data_json': static_plant_data_json})


def index(request):
    return render(request, 'index.html')
