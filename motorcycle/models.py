from django.db import models


class MotorcycleBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Motorcycle(models.Model):
    MOTORCYCLE_TYPES = [
        ('naked', 'Naked'),
        ('sport', 'Esportiva'),
        ('trail', 'Trail'),
        ('scooter', 'Scooter'),
        ('custom', 'Custom'),
        ('touring', 'Touring'),
    ]
    model = models.CharField(max_length=50)
    brand = models.ForeignKey(MotorcycleBrand, on_delete=models.PROTECT, related_name='MotorcycleBrand')
    type = models.CharField(max_length=20, choices=MOTORCYCLE_TYPES, null=True, blank=True)
    engine_cc = models.IntegerField(null=True, blank=True)
    factory_year = models.IntegerField(null=True, blank=True)
    model_year = models.IntegerField(null=True, blank=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='motorcycle/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'{self.brand} - {self.model} - {self.engine_cc}cc'
