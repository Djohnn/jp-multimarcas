from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MotorcycleBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['name']

    def __str__(self):
        return self.name


class Motorcycle(models.Model):

    class TypeChoices(models.TextChoices):
        NAKED = 'naked', 'Naked'
        SPORT = 'sport', 'Esportiva'
        TRAIL = 'trail', 'Trail'
        SCOOTER = 'scooter', 'Scooter'
        CUSTOM = 'custom', 'Custom'
        TOURING = 'touring', 'Touring'

    class FuelChoices(models.TextChoices):
        GASOLINA = 'gasolina', 'Gasolina'
        ETANOL = 'etanol', 'Etanol'
        FLEX = 'flex', 'Flex'
        ELETRICO = 'eletrico', 'Elétrico'

    class TransmissionChoices(models.TextChoices):
        MANUAL = 'manual', 'Manual'
        AUTOMATICO = 'automatico', 'Automático'
        SEMI_AUTOMATICO = 'semi_automatico', 'Semi-automático'

    class StatusChoices(models.TextChoices):
        DISPONIVEL = 'disponivel', 'Disponível'
        VENDIDO = 'vendido', 'Vendido'
        RESERVADO = 'reservado', 'Reservado'
        MANUTENCAO = 'manutencao', 'Em manutenção'

    # Dono do registro
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='motorcycles',
        null=True,
        blank=True
    )

    # Identificação
    brand = models.ForeignKey(
        MotorcycleBrand,
        on_delete=models.PROTECT,
        related_name='motorcycles'
    )
    model = models.CharField(max_length=80)
    version = models.CharField(max_length=80, blank=True, null=True)
    type = models.CharField(max_length=20, choices=TypeChoices.choices, null=True, blank=True)
    engine_cc = models.PositiveIntegerField(null=True, blank=True)
    factory_year = models.PositiveIntegerField(null=True, blank=True)
    model_year = models.PositiveIntegerField(null=True, blank=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)

    # Especificações
    fuel = models.CharField(max_length=20, choices=FuelChoices.choices, blank=True, null=True)
    transmission = models.CharField(max_length=20, choices=TransmissionChoices.choices, blank=True, null=True)
    mileage = models.PositiveIntegerField(help_text='Quilometragem em km', blank=True, null=True)

    # Comercial
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fipe_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.DISPONIVEL)

    # Histórico
    ipva_paid = models.BooleanField(default=False)
    licensed = models.BooleanField(default=True)
    single_owner = models.BooleanField(default=True)

    # Descrição
    bio = models.TextField(blank=True, null=True)

    # Imagem
    photo = models.ImageField(upload_to='motorcycle/', blank=True, null=True)

    # Controle
    is_featured = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Moto'
        verbose_name_plural = 'Motos'

    def __str__(self):
        return f'{self.brand} {self.model} {self.engine_cc}cc ({self.factory_year})'


class MotorcycleInventory(models.Model):
    motorcycle_count = models.IntegerField()
    motorcycle_value = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Inventário'
        verbose_name_plural = 'Inventários'

    def __str__(self):
        return f'{self.motorcycle_count} motos — R$ {self.motorcycle_value}'
