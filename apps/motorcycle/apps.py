from django.apps import AppConfig


class MotorcycleConfig(AppConfig):
    name = 'apps.motorcycle'

    def ready(self):
        import apps.motorcycle.signals