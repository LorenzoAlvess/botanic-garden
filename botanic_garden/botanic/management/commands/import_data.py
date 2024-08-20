import json
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from botanic.models import Family, Genus, Species

class Command(BaseCommand):
    help = 'Importa dados de famílias, gêneros e espécies a partir de arquivos JSON.'

    def add_arguments(self, parser):
        parser.add_argument('families_file', type=str, help='Caminho para o arquivo JSON com as famílias.')
        parser.add_argument('genera_file', type=str, help='Caminho para o arquivo JSON com os gêneros.')
        parser.add_argument('species_file', type=str, help='Caminho para o arquivo JSON com as espécies.')

    def handle(self, *args, **kwargs):
        families_file = kwargs['families_file']
        genera_file = kwargs['genera_file']
        species_file = kwargs['species_file']
        
        def load_json(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)

        def import_data():
            # Importar e inserir famílias
            families = load_json(families_file)
            for family_name in families:
                try:
                    Family.objects.create(name=family_name)
                    self.stdout.write(self.style.SUCCESS(f'Family added: {family_name}'))
                except IntegrityError:
                    self.stdout.write(self.style.WARNING(f'Family already exists: {family_name}'))

            # Importar e inserir gêneros
            genera = load_json(genera_file)
            for family_name, genus_list in genera.items():
                family, created = Family.objects.get_or_create(name=family_name)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Family created: {family_name}'))
                for genus_name in genus_list:
                    try:
                        Genus.objects.create(name=genus_name, family=family)
                        self.stdout.write(self.style.SUCCESS(f'Genus added: {genus_name} under family {family_name}'))
                    except IntegrityError:
                        self.stdout.write(self.style.WARNING(f'Genus already exists: {genus_name} under family {family_name}'))

            # Importar e inserir espécies
            species = load_json(species_file)
            for family_name, genera_dict in species.items():
                for genus_name, species_list in genera_dict.items():
                    genus = Genus.objects.filter(name=genus_name, family__name=family_name).first()
                    if genus:
                        for species_name in species_list:
                            try:
                                Species.objects.create(name=species_name, genus=genus)
                                self.stdout.write(self.style.SUCCESS(f'Species added: {species_name} under genus {genus_name}'))
                            except IntegrityError:
                                self.stdout.write(self.style.WARNING(f'Species already exists: {species_name} under genus {genus_name}'))
                    else:
                        self.stdout.write(self.style.ERROR(f'Genus not found: {genus_name} under family {family_name}'))

        import_data()
