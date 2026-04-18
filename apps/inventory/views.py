import json
from decimal import Decimal

from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from apps.cars.models import CarInventory
from apps.motorcycle.models import MotorcycleInventory


class InventoryDashboardView(TemplateView):
    template_name = 'inventory/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        selected_type = self.request.GET.get('type', 'all')
        selected_date_start = self.request.GET.get('date_start', '')
        selected_date_end = self.request.GET.get('date_end', '')
        page_number = self.request.GET.get('page', 1)

        car_qs = CarInventory.objects.all()
        motorcycle_qs = MotorcycleInventory.objects.all()

        if selected_date_start:
            car_qs = car_qs.filter(created_at__gte=selected_date_start)
            motorcycle_qs = motorcycle_qs.filter(created_at__gte=selected_date_start)

        if selected_date_end:
            car_qs = car_qs.filter(created_at__lte=selected_date_end)
            motorcycle_qs = motorcycle_qs.filter(created_at__lte=selected_date_end)

        latest_car = car_qs.first()
        latest_motorcycle = motorcycle_qs.first()

        current_cars_count = latest_car.cars_count if latest_car else 0
        current_cars_value = latest_car.cars_value if latest_car else Decimal('0.00')

        current_motorcycles_count = latest_motorcycle.motorcycle_count if latest_motorcycle else 0
        current_motorcycles_value = latest_motorcycle.motorcycle_value if latest_motorcycle else Decimal('0.00')

        total_vehicles_count = current_cars_count + current_motorcycles_count
        total_inventory_value = current_cars_value + current_motorcycles_value

        # gráfico
        car_history_for_chart = list(car_qs.order_by('created_at')[:30])
        motorcycle_history_for_chart = list(motorcycle_qs.order_by('created_at')[:30])

        all_dates = sorted({
            item.created_at.strftime('%d/%m/%Y') for item in car_history_for_chart
        } | {
            item.created_at.strftime('%d/%m/%Y') for item in motorcycle_history_for_chart
        })

        car_map = {
            item.created_at.strftime('%d/%m/%Y'): float(item.cars_value)
            for item in car_history_for_chart
        }
        motorcycle_map = {
            item.created_at.strftime('%d/%m/%Y'): float(item.motorcycle_value)
            for item in motorcycle_history_for_chart
        }

        chart_labels = []
        chart_car_values = []
        chart_motorcycle_values = []

        for date_label in all_dates:
            chart_labels.append(date_label)
            chart_car_values.append(car_map.get(date_label, 0))
            chart_motorcycle_values.append(motorcycle_map.get(date_label, 0))

        # histórico
        combined_history = []

        if selected_type in ['all', 'car']:
            for item in car_qs:
                combined_history.append({
                    'created_at': item.created_at,
                    'vehicle_type': 'Carros',
                    'quantity': item.cars_count,
                    'total_value': item.cars_value,
                })

        if selected_type in ['all', 'motorcycle']:
            for item in motorcycle_qs:
                combined_history.append({
                    'created_at': item.created_at,
                    'vehicle_type': 'Motos',
                    'quantity': item.motorcycle_count,
                    'total_value': item.motorcycle_value,
                })

        combined_history.sort(key=lambda item: item['created_at'], reverse=True)

        paginator = Paginator(combined_history, 10)
        page_obj = paginator.get_page(page_number)

        context['current_cars_count'] = current_cars_count
        context['current_cars_value'] = current_cars_value
        context['current_motorcycles_count'] = current_motorcycles_count
        context['current_motorcycles_value'] = current_motorcycles_value
        context['total_vehicles_count'] = total_vehicles_count
        context['total_inventory_value'] = total_inventory_value

        context['selected_type'] = selected_type
        context['selected_date_start'] = selected_date_start
        context['selected_date_end'] = selected_date_end

        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()

        context['chart_labels'] = mark_safe(json.dumps(chart_labels))
        context['chart_car_values'] = mark_safe(json.dumps(chart_car_values))
        context['chart_motorcycle_values'] = mark_safe(json.dumps(chart_motorcycle_values))

        return context