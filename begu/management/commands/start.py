from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'flush, makemigrations, migrate and runserver'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Flushing database...'))
        call_command('flush', interactive=False)

        self.stdout.write(self.style.SUCCESS('Making migrations...'))
        call_command('makemigrations')
    
        self.stdout.write(self.style.SUCCESS('Migrating database...'))
        call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Running server...'))
        call_command('runserver')