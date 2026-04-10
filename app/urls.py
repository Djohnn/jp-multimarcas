from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('account/', include('account.urls')),
    path('motorcycle/', include('motorcycle.urls')),

    path('', lambda request: redirect('/cars')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
