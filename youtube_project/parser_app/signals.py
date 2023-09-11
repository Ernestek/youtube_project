from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserTariff

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_tariff(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: UserTariff.objects.create(user=instance))
        # UserTariff.objects.create(user=instance)
