from django.contrib import admin
from apps.motorcycle.models import Motorcycle, MotorcycleBrand, MotorcycleInventory


@admin.register(MotorcycleBrand)
class MotorcycleBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'type', 'engine_cc', 'factory_year',
                    'model_year', 'fuel', 'transmission', 'status',
                    'sale_price', 'is_featured', 'is_visible')
    list_filter = ('status', 'fuel', 'transmission', 'type', 'is_featured', 'is_visible', 'brand')
    search_fields = ('model', 'plate')
    list_editable = ('is_featured', 'is_visible', 'status')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identificação', {
            'fields': ('brand', 'model', 'version', 'type', 'engine_cc',
                      'factory_year', 'model_year', 'plate', 'color')
        }),
        ('Especificações', {
            'fields': ('fuel', 'transmission', 'mileage')
        }),
        ('Comercial', {
            'fields': ('purchase_price', 'sale_price', 'fipe_value', 'status')
        }),
        ('Histórico', {
            'fields': ('ipva_paid', 'licensed', 'single_owner')
        }),
        ('Mídia e Descrição', {
            'fields': ('photo', 'bio')
        }),
        ('Controle', {
            'fields': ('user', 'is_featured', 'is_visible', 'created_at', 'updated_at')
        }),
    )


@admin.register(MotorcycleInventory)
class MotorcycleInventoryAdmin(admin.ModelAdmin):
    list_display = ('motorcycle_count', 'motorcycle_value', 'created_at')
    readonly_fields = ('created_at',)