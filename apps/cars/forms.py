from django import forms
from apps.cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Car
        fields = [
            'brand',
            'model',
            'version',
            'factory_year',
            'model_year',
            'plate',
            'color',
            'doors',
            'fuel',
            'transmission',
            'mileage',
            'body_type',
            'sale_price',
            'fipe_value',
            'status',
            'ipva_paid',
            'licensed',
            'single_owner',
            'photo',
            'bio',
        ]

    def clean_sale_price(self):
        sale_price = self.cleaned_data.get('sale_price')
        if sale_price and sale_price < 20000:
            self.add_error('sale_price', 'Valor do carro deve ser maior que R$ 20.000')
        return sale_price

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year and factory_year < 1980:
            self.add_error('factory_year', 'Não é possível cadastrar carros anteriores a 1980')
        return factory_year
    
    def clean(self):
        cleaned_data = super().clean()
        # Se for uma edição, valida se o dono permanece o mesmo
        if self.instance.pk:
            if self.instance.user != self.user:
                raise forms.ValidationError("Ação não autorizada.")
        return cleaned_data


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']