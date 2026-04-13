from django import forms
from apps.leads.models import Lead
from apps.cars.models import Car
from apps.motorcycle.models import Motorcycle


class LeadStatusForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['status', 'assigned_to']


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = ["name", "phone", "email", "message", "car", "motorcycle"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["car"].required = False
        self.fields["motorcycle"].required = False
        self.fields["car"].widget = forms.HiddenInput()
        self.fields["motorcycle"].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super().clean()
        car = cleaned_data.get("car")
        motorcycle = cleaned_data.get("motorcycle")

        if car and motorcycle:
            raise forms.ValidationError("Selecione apenas um veículo.")

        if not car and not motorcycle:
            raise forms.ValidationError("Você precisa selecionar um veículo.")

        return cleaned_data

    def clean_car(self):
        car = self.cleaned_data.get("car")
        if car and not Car.objects.filter(id=car.id).exists():
            raise forms.ValidationError("Carro inválido.")
        return car

    def clean_motorcycle(self):
        motorcycle = self.cleaned_data.get("motorcycle")
        if motorcycle and not Motorcycle.objects.filter(id=motorcycle.id).exists():
            raise forms.ValidationError("Moto inválida.")
        return motorcycle

    def save(self, commit=True):
        lead = super().save(commit=False)
        if self.user and self.user.is_authenticated:
            lead.assigned_to = self.user
        if commit:
            lead.save()
        return lead