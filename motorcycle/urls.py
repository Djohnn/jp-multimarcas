from django.urls import path
from motorcycle.views import MotorcycleListView, NewMotorcycleCreateView, NewMotorcycleBrandCreateView

urlpatterns = [
    path('', MotorcycleListView.as_view(), name='motorcycle_list'),
    path('new_motorcycle/', NewMotorcycleCreateView.as_view(), name='new_motorcycle'),
    path('new_motorcycle_brand/', NewMotorcycleBrandCreateView.as_view(), name='new_motorcycle_brand'),
]
