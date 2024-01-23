from django.db import transaction
from .models import Family, Genus, Species, Collection

@transaction.atomic
def create_seed_data():
    # Criar algumas famílias
    family1 = Family.objects.create(name='Rosaceae')
    family2 = Family.objects.create(name='Lamiaceae')

    # Criar alguns gêneros
    genus1 = Genus.objects.create(name='Rosa', family=family1)
    genus2 = Genus.objects.create(name='Lavandula', family=family2)

    # Criar algumas espécies
    species1 = Species.objects.create(name='Malus domestica', genus=genus1)
    species2 = Species.objects.create(name='Lavandula angustifolia', genus=genus2)

    # Criar algumas coleções
    collection1 = Collection.objects.create(name='Coleção 1', description='Descrição da coleção 1')
    collection2 = Collection.objects.create(name='Coleção 2', description='Descrição da coleção 2')

    # Adicionar espécies às coleções
    species1.collections.add(collection1)
    species2.collections.add(collection2)

if __name__ == '__main__':
    create_seed_data()
    print('Dados de semente para Botanic criados com sucesso!')
