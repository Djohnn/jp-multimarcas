from django.apps import AppConfig


class MotorcycleConfig(AppConfig):
    name = 'motorcycle'

    def ready(self):
        import motorcycle.signals