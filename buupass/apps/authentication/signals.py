from django.dispatch import receiver
from django.db.models.signals import post_save
from mpesa.apps.wallet.models import Wallet
from mpesa.apps.authentication.models import User



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        import pdb
        pdb.set_trace()
        