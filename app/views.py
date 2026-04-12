from django.views.generic import TemplateView
from django.db.models import Q
from apps.cars.models import Car, CarInventory, Brand
from apps.motorcycle.models import Motorcycle, MotorcycleInventory


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtros
        brand_id = self.request.GET.get('brand')
        model = self.request.GET.get('model')
        price_max = self.request.GET.get('price_max')
        body_type = self.request.GET.get('body_type')

        cars = Car.objects.all()

        if brand_id:
            cars = cars.filter(brand__id=brand_id)
        if model:
            cars = cars.filter(model__icontains=model)
        if price_max:
            cars = cars.filter(value__lte=price_max)
        if body_type:
            cars = cars.filter(body_type=body_type)

        context['latest_cars'] = Car.objects.order_by('-id')[:3]
        context['latest_motorcycles'] = Motorcycle.objects.order_by('-id')[:3]
        context['cars_count'] = Car.objects.count()
        context['motorcycles_count'] = Motorcycle.objects.count()
        context['brands'] = Brand.objects.all().order_by('name')
        context['filtered_cars'] = cars.order_by('-id')
        context['body_types'] = Car.BODY_TYPES
        context['selected_brand'] = brand_id
        context['selected_body_type'] = body_type
        context['selected_price_max'] = price_max or 500000
        return context