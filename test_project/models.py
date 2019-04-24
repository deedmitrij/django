from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


# class User(AbstractUser):
#     avatar = models.ImageField()


class Participant(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self): return f'{self.name}'


class Measurement(models.Model):
    date = models.DateTimeField(null=False, default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    user_id = models.ForeignKey('Participant', related_name='measurements', on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self): return f'Weight: {self.weight}, user: {self.user}'
    def __str__(self): return f'Weight: {self.weight}'

# Auto-creating tokens for all users

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
