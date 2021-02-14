from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save

from buupass.helpers.fancy_generator import fancy_id_generator


class User(AbstractUser):
    class Types(models.TextChoices):
        NANNY = "NANNY", "Nanny"
        OWNER = "ONWER", "Owner"

    base_type = "NONE"

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    id = models.CharField(db_index=True,
                          max_length=256,
                          default=fancy_id_generator,
                          primary_key=True,
                          editable=False)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    email = models.CharField(blank=False, max_length=300, unique=True)
    phone_number = models.IntegerField(blank=False, default=254000000)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    @staticmethod
    def get_user(email):
        try:
            user = User.objects.get(email=email)
            return user

        except Exception:
            return False


class OwnerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            type=User.Types.OWNER)


class NannyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            type=User.Types.NANNY)


class NannyMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Nanny(User):
    base_type = User.Types.NANNY
    objects = NannyManager()

    class Meta:
        proxy = True


class OwnerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Owner(User):
    base_type = User.Types.OWNER
    objects = OwnerManager()

    @property
    def more(self):
        return self.OwnerMore

    class Meta:
        proxy = True
