from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    BODY_TYPES = [
        ('hatch', 'Hatch'),
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('pickup', 'Caminhonete'),
        ('utility', 'Utilitário'),
        ('station_wagon', 'Station Wagon'),
    ]
    id = models.AutoField(primary_key=True)
    body_type = models.CharField(max_length=20, choices=BODY_TYPES, null=True, blank=True)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(null=True, blank=True)
    model_year = models.IntegerField(null=True, blank=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
    

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'