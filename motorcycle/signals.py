from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from motorcycle.models import Motorcycle, MotorcycleInventory
from gemini_api.client import get_motorcycle_ai_bio




def motorcycle_inventory_update():
    motorcycle_count = Motorcycle.objects.all().count()
    motorcycle_value = Motorcycle.objects.aggregate(
        total_value=Sum('value')
        )['total_value']
    MotorcycleInventory.objects.create(
        motorcyclecount=motorcycle_count,
        motorcycle_value=motorcycle_value
    )



@receiver(pre_save, sender=Motorcycle)
def motorcycle_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_motorcycle_ai_bio(
            instance.model,
            instance.brand,
            instance.model_year,
            instance.get_type_display(),
            instance.engine_cc,
        )
        instance.bio = ai_bio

@receiver(post_save, sender=Motorcycle)
def motorcycle_post_save(sender, instance, **kwargs):
    motorcycle_inventory_update()



@receiver(post_delete, sender=Motorcycle)
def motorcycle_post_delete(sender, instance, **kwargs):
    motorcycle_inventory_update()

