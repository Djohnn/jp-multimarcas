from django.contrib import admin
from apps.cars.models import Car, Brand, CarInventory


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'fuel',
                    'transmission', 'status', 'sale_price', 'is_featured', 'is_visible')
    list_filter = ('status', 'fuel', 'transmission', 'body_type', 'is_featured', 'is_visible', 'brand')
    search_fields = ('model', 'plate', 'chassis')
    list_editable = ('is_featured', 'is_visible', 'status')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identificação', {
            'fields': ('brand', 'model', 'version', 'factory_year', 'model_year', 'plate', 'chassis', 'color', 'doors')
        }),
        ('Especificações', {
            'fields': ('fuel', 'transmission', 'mileage', 'body_type')
        }),
        ('Comercial', {
            'fields': ('purchase_price', 'sale_price', 'fipe_value', 'status')
        }),
        ('Histórico', {
            'fields': ('ipva_paid', 'licensed', 'single_owner', 'accident_history')
        }),
        ('Mídia e Descrição', {
            'fields': ('photo', 'bio')
        }),
        ('Controle', {
            'fields': ('user', 'is_featured', 'is_visible', 'created_at', 'updated_at')
        }),
    )


@admin.register(CarInventory)
class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('cars_count', 'cars_value', 'created_at')
    readonly_fields = ('created_at',)