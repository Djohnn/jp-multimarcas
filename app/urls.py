from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('cars/', include('apps.cars.urls')),
    path('account/', include('apps.account.urls')),
    path('motorcycle/', include('apps.motorcycle.urls')),
    path('leads/', include('apps.leads.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
