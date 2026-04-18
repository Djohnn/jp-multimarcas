from django.views.generic import TemplateView
from apps.cars.models import Car, Brand
from apps.motorcycle.models import Motorcycle



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtros
        vehicle_type = self.request.GET.get('vehicle_type')
        brand_id = self.request.GET.get('brand')
        model = self.request.GET.get('model')
        price_min = self.request.GET.get('price_min')
        price_max = self.request.GET.get('price_max')
        body_type = self.request.GET.get('body_type')

        filtered_cars = Car.objects.none()
        filtered_motorcycles = Motorcycle.objects.none()

        # Filtrar carros
        if vehicle_type == 'car':
            filtered_cars = Car.objects.all()

            if brand_id:
                filtered_cars = filtered_cars.filter(brand__id=brand_id)

            if model:
                filtered_cars = filtered_cars.filter(model__icontains=model)

            if price_min:
                try:
                    filtered_cars = filtered_cars.filter(sale_price__gte=float(price_min))
                except (ValueError, TypeError):
                    price_min = ''

            if price_max:
                try:
                    filtered_cars = filtered_cars.filter(sale_price__lte=float(price_max))
                except (ValueError, TypeError):
                    price_max = ''

            if body_type:
                filtered_cars = filtered_cars.filter(body_type=body_type)

            filtered_cars = filtered_cars.order_by('-id')

        # Filtrar motos
        elif vehicle_type == 'motorcycle':
            filtered_motorcycles = Motorcycle.objects.all()

            if brand_id:
                filtered_motorcycles = filtered_motorcycles.filter(brand__id=brand_id)

            if model:
                filtered_motorcycles = filtered_motorcycles.filter(model__icontains=model)

            if price_min:
                try:
                    filtered_motorcycles = filtered_motorcycles.filter(sale_price__gte=float(price_min))
                except (ValueError, TypeError):
                    price_min = ''

            if price_max:
                try:
                    filtered_motorcycles = filtered_motorcycles.filter(sale_price__lte=float(price_max))
                except (ValueError, TypeError):
                    price_max = ''

            filtered_motorcycles = filtered_motorcycles.order_by('-id')

        context['latest_cars'] = Car.objects.order_by('-id')[:4]
        context['latest_motorcycles'] = Motorcycle.objects.order_by('-id')[:4]
        context['cars_count'] = Car.objects.count()
        context['motorcycles_count'] = Motorcycle.objects.count()
        context['brands'] = Brand.objects.all().order_by('name')

        context['filtered_cars'] = filtered_cars
        context['filtered_motorcycles'] = filtered_motorcycles

        context['body_types'] = Car.BodyTypeChoices.choices
        context['selected_vehicle_type'] = vehicle_type
        context['selected_brand'] = brand_id
        context['selected_body_type'] = body_type
        context['selected_price_min'] = price_min or ''
        context['selected_price_max'] = price_max or ''

        return context