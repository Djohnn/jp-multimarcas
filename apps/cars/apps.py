from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'apps.cars'

    def ready(self):
        import apps.cars.signal
