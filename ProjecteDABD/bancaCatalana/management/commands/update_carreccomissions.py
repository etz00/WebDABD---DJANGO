from django.core.management.base import BaseCommand
from bancaCatalana.models import Operacio, CarrecComissions, Compte
from faker import Faker

fake = Faker('es_ES')

class Command(BaseCommand):
    help = 'Actualizar campos nulos de CarrecComissions'

    def handle(self, *args, **kwargs):
        default_compte, created = Compte.objects.get_or_create(
            iban='default_IBAN',
            defaults={
                'data_obertura': '2024-01-01',
                'saldo': 0,
                'entidad': 'default_entidad',
                'nif_id': 'default_NIF'
            }
        )
        
        for comision in CarrecComissions.objects.filter(id_operacio__isnull=True):
            operacion = Operacio.objects.create(data=fake.date_between(start_date='-1y', end_date='today'), import_real=0, IBAN_origen=default_compte)
            comision.id_operacio = operacion
            comision.save()
        self.stdout.write(self.style.SUCCESS('Campos actualizados exitosamente.'))
