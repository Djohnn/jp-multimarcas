from django.urls import path
from apps.leads.views import LeadCreateView

urlpatterns = [
    path('new/', LeadCreateView.as_view(), name='lead_create'),
]