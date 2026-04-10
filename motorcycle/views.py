from motorcycle.models import Motorcycle, MotorcycleBrand
from motorcycle.forms import MotorcycleBrandModelForm, MotorcycleModelForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView



class MotorcycleListView(ListView):
    model = Motorcycle
    template_name = 'motorcycle.html'
    context_object_name = 'motorcycle'

    def get_queryset(self):
        motorcycles = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            motorcycles = motorcycles.filter(model__icontains=search)
        return motorcycles
    

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