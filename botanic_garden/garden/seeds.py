from django.db import transaction
from botanic.models import Species
from .models import Event, Garden, PlantInGarden

@transaction.atomic
def create_seed_data():
    # Criar alguns eventos
    event1 = Event.objects.create(name='Evento 1', date='2023-01-01', description='Descrição do evento 1')
    event2 = Event.objects.create(name='Evento 2', date='2023-02-01', description='Descrição do evento 2')

    # Criar alguns jardins
    garden1 = Garden.objects.create(name='Jardim 1', location='Localização 1')
    garden2 = Garden.objects.create(name='Jardim 2', location='Localização 2')

    # Adicionar eventos aos jardins
    garden1.events.add(event1)
    garden2.events.add(event2)

    # Criar algumas plantas
    plant1 = Species.objects.create(name='Malus domestica').plants.create(quantity=10)
    plant2 = Species.objects.create(name='Lavandula angustifolia').plants.create(quantity=5)

    # Adicionar plantas aos jardins
    PlantInGarden.objects.create(garden=garden1, plant=plant1)
    PlantInGarden.objects.create(garden=garden2, plant=plant2)

if __name__ == '__main__':
    create_seed_data()
    print('Dados de semente para Garden criados com sucesso!')
