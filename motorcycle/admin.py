from django.contrib import admin
from motorcycle.models import Motorcycle, MotorcycleBrand

class MotorcycleBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'type', 'engine_cc', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)


admin.site.register(MotorcycleBrand, MotorcycleBrandAdmin)
admin.site.register(Motorcycle, MotorcycleAdmin)