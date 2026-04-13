from django.urls import path
from apps.leads.views import LeadCreateView, LeadListView, LeadUpdateStatusView

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('new/', LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/status/', LeadUpdateStatusView.as_view(), name='lead_update_status'),
]