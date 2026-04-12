from django.urls import path
from motorcycle.views import MotorcycleListView, NewMotorcycleCreateView, NewMotorcycleBrandCreateView, MotorcycleDetailView, MotorcycleUpdateView, MotorcycleDeleteView

urlpatterns = [
    path('', MotorcycleListView.as_view(), name='motorcycle_list'),
    path('new_motorcycle/', NewMotorcycleCreateView.as_view(), name='new_motorcycle'),
    path('new_motorcycle_brand/', NewMotorcycleBrandCreateView.as_view(), name='new_motorcycle_brand'),
        path('motorcycle/<int:pk>/', MotorcycleDetailView.as_view(), name='motorcycle_detail'),
    path('motocycle/<int:pk>/update/', MotorcycleUpdateView.as_view(), name='motorcycle_update'),
    path('motorcycle/<int:pk>/delete/', MotorcycleDeleteView.as_view(), name='motorcycle_delete'),
]

