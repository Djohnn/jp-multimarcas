from motorcycle.models import Motorcycle, MotorcycleBrand
from motorcycle.forms import MotorcycleBrandModelForm, MotorcycleModelForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse


class MotorcycleListView(ListView):
    model = Motorcycle
    template_name = 'motorcycle.html'
    context_object_name = 'motorcycles'
    paginate_by = 12

    def get_queryset(self):
        motorcycles = super().get_queryset()
        search = self.request.GET.get('search')
        order = self.request.GET.get('order', 'model')

        if search:
            motorcycles = motorcycles.filter(model__icontains=search)

        ordering = {
            'model': 'model',
            'price_asc': 'value',
            'price_desc': '-value',
            'year_asc': 'factory_year',
            'year_desc': '-factory_year',
        }
        motorcycles = motorcycles.order_by(ordering.get(order, 'model'))
        return motorcycles
    
class MotorcycleDetailView(DetailView):
    model = Motorcycle
    template_name = 'motorcycle_detail.html'
    

@method_decorator(login_required(login_url='/account/login/'), name='dispatch')   
class NewMotorcycleCreateView(CreateView):
    model = Motorcycle
    form_class = MotorcycleModelForm
    template_name = "new_motorcycle.html"
    success_url = '/motorcycle/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_form'] = MotorcycleBrandModelForm()
        return context
    
    
@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
@method_decorator(staff_member_required, name='dispatch')    
class NewMotorcycleBrandCreateView(CreateView):
    model = MotorcycleBrand
    form_class = MotorcycleBrandModelForm
    template_name = 'new_motorcycle_brand.html'
    success_url = '/motorcycle/new_motorcycle/'

@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class MotorcycleUpdateView(UpdateView):
    model = Motorcycle
    form_class = MotorcycleModelForm
    template_name = 'motorcycle_update.html'
    
    def get_success_url(self):
        return reverse('motorcycle_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class MotorcycleDeleteView(DeleteView):
    model = Motorcycle
    template_name = 'motorcycle_delete.html'
    success_url = '/motorcycle/'