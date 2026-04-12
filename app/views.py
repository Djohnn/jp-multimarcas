from django.views.generic import TemplateView
from cars.models import Car, CarInventory
from motorcycle.models import Motorcycle, MotorcycleInventory


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_cars'] = Car.objects.order_by('-id')[:3]
        context['latest_motorcycles'] = Motorcycle.objects.order_by('-id')[:3]
        context['cars_count'] = Car.objects.count()
        context['motorcycles_count'] = Motorcycle.objects.count()
        return context