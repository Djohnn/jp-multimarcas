from django.views.generic import CreateView
from django.urls import reverse
from apps.leads.models import Lead
from apps.leads.forms import LeadForm


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/lead_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['car'] = self.request.GET.get('car')
        initial['motorcycle'] = self.request.GET.get('motorcycle')
        return initial

    def get_success_url(self):
        car = self.object.car
        motorcycle = self.object.motorcycle
        if car:
            return reverse('car_detail', kwargs={'pk': car.pk})
        return reverse('motorcycle_detail', kwargs={'pk': motorcycle.pk})