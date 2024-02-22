from django.apps import AppConfig


class BeguConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'begu'

    def ready(self):
        import begu.signals  
