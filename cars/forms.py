from django import forms
from cars.models import Brand, Car

#forma manua de escrever form ultilizando somento forms.form o que acaba sendo muito trabalhoso e muitas linhas de codigos.

# class CarForm(forms.Form):
#     model = forms.CharField(max_length=100)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     image = forms.ImageField()

#     def save(self):
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save()
#         return car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor do carro deve ser maior que 20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1980:
            self.add_error('factory_year', 'Não e possivel cadastro de carros anterior a 1980')
        return factory_year
    

class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'