from django.views.generic import CreateView, ListView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from urllib.parse import quote
from django.urls import reverse_lazy
from apps.leads.models import Lead
from apps.leads.forms import LeadForm, LeadStatusForm


@method_decorator(staff_member_required, name='dispatch')
class LeadListView(ListView):
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'
    paginate_by = 20

    def get_queryset(self):
        leads = Lead.objects.all()
        status = self.request.GET.get('status')
        if status:
            leads = leads.filter(status=status)
        return leads

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Lead.Status.choices
        context['selected_status'] = self.request.GET.get('status', '')
        context['total'] = Lead.objects.count()
        context['count_new'] = Lead.objects.filter(status=Lead.Status.NEW).count()
        context['count_contacted'] = Lead.objects.filter(status=Lead.Status.CONTACTED).count()
        context['count_negotiating'] = Lead.objects.filter(status=Lead.Status.NEGOTIATING).count()
        context['count_closed'] = Lead.objects.filter(status=Lead.Status.CLOSED).count()
        context['count_lost'] = Lead.objects.filter(status=Lead.Status.LOST).count()
        return context


@method_decorator(staff_member_required, name='dispatch')
class LeadUpdateStatusView(UpdateView):
    model = Lead
    form_class = LeadStatusForm
    template_name = 'leads/lead_status_form.html'
    success_url = reverse_lazy('lead_list')


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return self._whatsapp_url()

    def _whatsapp_url(self):
        lead = self.object
        if lead.car:
            msg = (
                f"Olá! Me chamo {lead.name} e tenho interesse no "
                f"{lead.car.brand} {lead.car.model} "
                f"{lead.car.factory_year}/{lead.car.model_year}. "
                f"Preço: R$ {lead.car.sale_price}. "
                f"Pode me passar mais informações?"
            )
        else:
            msg = (
                f"Olá! Me chamo {lead.name} e tenho interesse na "
                f"{lead.motorcycle.brand} {lead.motorcycle.model} "
                f"{lead.motorcycle.factory_year}. "
                f"Preço: R$ {lead.motorcycle.sale_price}. "
                f"Pode me passar mais informações?"
            )
        return f"https://wa.me/{settings.WHATSAPP_NUMBER}?text={quote(msg)}"