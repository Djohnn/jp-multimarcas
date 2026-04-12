from django.urls import path
from apps.motorcycle.views import (
    MotorcycleListView,
    MotorcycleCreateView,
    MotorcycleBrandCreateView,
    MotorcycleDetailView,
    MotorcycleUpdateView,
    MotorcycleDeleteView,
)


urlpatterns = [
    path('', MotorcycleListView.as_view(), name='motorcycle_list'),

    path('create/', MotorcycleCreateView.as_view(), name='motorcycle_create'),
    path('brand/create/', MotorcycleBrandCreateView.as_view(), name='motorcycle_brand_create'),

    path('<int:pk>/', MotorcycleDetailView.as_view(), name='motorcycle_detail'),
    path('<int:pk>/update/', MotorcycleUpdateView.as_view(), name='motorcycle_update'),
    path('<int:pk>/delete/', MotorcycleDeleteView.as_view(), name='motorcycle_delete'),
]


