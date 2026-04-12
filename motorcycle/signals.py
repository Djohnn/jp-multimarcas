from django.db.models.signals import pre_save
from django.dispatch import receiver
from motorcycle.models import Motorcycle
from gemini_api.client import get_motorcycle_ai_bio


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