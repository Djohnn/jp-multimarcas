from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['name']

    def __str__(self):
        return self.name


class Car(models.Model):

    class FuelChoices(models.TextChoices):
        GASOLINA = "gasolina", "Gasolina"
        ETANOL = "etanol", "Etanol"
        FLEX = "flex", "Flex"
        DIESEL = "diesel", "Diesel"
        ELETRICO = "eletrico", "Elétrico"
        HIBRIDO = "hibrido", "Híbrido"

    class TransmissionChoices(models.TextChoices):
        MANUAL = "manual", "Manual"
        AUTOMATICO = "automatico", "Automático"
        CVT = "cvt", "CVT"

    class StatusChoices(models.TextChoices):
        DISPONIVEL = "disponivel", "Disponível"
        VENDIDO = "vendido", "Vendido"
        RESERVADO = "reservado", "Reservado"
        MANUTENCAO = "manutencao", "Em manutenção"

    class BodyTypeChoices(models.TextChoices):
        HATCH = "hatch", "Hatch"
        SEDAN = "sedan", "Sedan"
        SUV = "suv", "SUV"
        PICKUP = "pickup", "Caminhonete"
        UTILITY = "utility", "Utilitário"
        STATION_WAGON = "station_wagon", "Station Wagon"

    # Dono do registro
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars", null=True, blank=True)

    # Identificação
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    model = models.CharField(max_length=80)
    version = models.CharField(max_length=80, blank=True, null=True)
    factory_year = models.PositiveIntegerField(null=True, blank=True)
    model_year = models.PositiveIntegerField(null=True, blank=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    chassis = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    doors = models.PositiveIntegerField(default=4)

    # Especificações
    fuel = models.CharField(max_length=20, choices=FuelChoices.choices, blank=True, null=True)
    transmission = models.CharField(max_length=20, choices=TransmissionChoices.choices, blank=True, null=True)
    mileage = models.PositiveIntegerField(help_text="Quilometragem em km", blank=True, null=True)
    body_type = models.CharField(max_length=20, choices=BodyTypeChoices.choices, blank=True, null=True)

    # Comercial
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fipe_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.DISPONIVEL)

    # Histórico
    ipva_paid = models.BooleanField(default=False)
    licensed = models.BooleanField(default=True)
    single_owner = models.BooleanField(default=True)
    accident_history = models.TextField(blank=True, null=True)

    # Descrição
    bio = models.TextField(blank=True, null=True)

    # Imagem
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    # Controle
    is_featured = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.brand} {self.model} ({self.factory_year})'


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Inventário'
        verbose_name_plural = 'Inventários'

    def __str__(self):
        return f'{self.cars_count} carros — R$ {self.cars_value}'