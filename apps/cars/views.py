from apps.cars.models import Car, Brand
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from apps.cars.forms import CarModelForm, BrandModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
    
class CarsListView(ListView):
    model = Car
    template_name = 'cars/cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        cars = super().get_queryset()
        search = self.request.GET.get('search')
        order = self.request.GET.get('order', 'model')

        if search:
            cars = cars.filter(model__icontains=search)

        ordering = {
            'model': 'model',
            'price_asc': 'value',
            'price_desc': '-value',
            'year_asc': 'factory_year',
            'year_desc': '-factory_year',
        }
        cars = cars.order_by(ordering.get(order, 'model'))
        return cars
    
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        context['whatsapp_number'] = settings.WHATSAPP_NUMBER
        context['mensagem_whatsapp'] = (
            f"Olá! Tenho interesse no {car.brand} {car.model} "
            f"{car.factory_year}/{car.model_year}. "
            f"Preço: R$ {car.sale_price}. "
            f"Pode me passar mais informações?"
        )
        return context


@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'cars/new_car.html'
    success_url = '/cars/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_form'] = BrandModelForm()
        return context
    

@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
@method_decorator(staff_member_required, name='dispatch')
class NewBrandCreateView(CreateView):
    model = Brand
    form_class = BrandModelForm
    template_name = 'cars/new_brand.html'
    success_url = reverse_lazy('new_car')


@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'cars/car_update.html'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    success_url = '/cars/'