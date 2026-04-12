from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from apps.motorcycle.models import Motorcycle, MotorcycleBrand
from apps.motorcycle.forms import MotorcycleModelForm, MotorcycleBrandModelForm


class MotorcycleListView(ListView):
    model = Motorcycle
    template_name = 'motorcycle/motorcycle_list.html'
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
    template_name = 'motorcycle/motorcycle_detail.html'
    context_object_name = 'motorcycle'
    

@method_decorator(login_required(login_url='/account/login/'), name='dispatch')   
class MotorcycleCreateView(CreateView):
    model = Motorcycle
    form_class = MotorcycleModelForm
    template_name = "motorcycle/motorcycle_form.html"
    success_url = reverse_lazy('motorcycle_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_form'] = MotorcycleBrandModelForm()
        return context
    
    
@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
@method_decorator(staff_member_required, name='dispatch')    
class MotorcycleBrandCreateView(CreateView):
    model = MotorcycleBrand
    form_class = MotorcycleBrandModelForm
    template_name = 'motorcycle/brand_form.html'
    success_url = reverse_lazy('motorcycle_create')

@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class MotorcycleUpdateView(UpdateView):
    model = Motorcycle
    form_class = MotorcycleModelForm
    template_name = 'motorcycle/motorcycle_update.html'
    
    def get_success_url(self):
        return reverse_lazy('motorcycle_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/account/login/'), name='dispatch')
class MotorcycleDeleteView(DeleteView):
    model = Motorcycle
    template_name = 'motorcycle/motorcycle_confirm_delete.html'
    success_url = reverse_lazy('motorcycle_list')