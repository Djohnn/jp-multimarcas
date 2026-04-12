from django.forms import ModelForm
from apps.motorcycle.models import Motorcycle, MotorcycleBrand


class MotorcycleModelForm(ModelForm):
    class Meta:
        model = Motorcycle
        fields = '__all__'


class MotorcycleBrandModelForm(ModelForm):
    class Meta:
        model = MotorcycleBrand
        fields = '__all__'