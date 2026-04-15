from django.forms import ModelForm
from django.core.exceptions import ValidationError
from apps.motorcycle.models import Motorcycle, MotorcycleBrand


class MotorcycleModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


    class Meta:
        model = Motorcycle
        fields = [
            'brand',
            'model',
            'version',
            'type',
            'engine_cc',
            'factory_year',
            'model_year',
            'plate',
            'color',
            'fuel',
            'transmission',
            'mileage',
            'sale_price',
            'fipe_value',
            'status',
            'ipva_paid',
            'licensed',
            'single_owner',
            'photo',
            'bio',
        ]

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year and factory_year < 1980:
            self.add_error('factory_year', 'Não é possível cadastrar motos anteriores a 1980')
        return factory_year

    def clean_sale_price(self):
        sale_price = self.cleaned_data.get('sale_price')
        if sale_price and sale_price < 1000:
            self.add_error('sale_price', 'Valor da moto deve ser maior que R$ 1.000')
        return sale_price
    
    def clean(self):
        cleaned_data = super().clean()
        # Se for uma edição, valida se o dono permanece o mesmo
        if self.instance.pk:
            if self.instance.user != self.user:
                raise ValidationError("Ação não autorizada.")
        return cleaned_data


class MotorcycleBrandModelForm(ModelForm):
    class Meta:
        model = MotorcycleBrand
        fields = ['name']