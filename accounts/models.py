from django.db import models
from django.conf import settings
# Create your models here.


class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sellers')

    def __str__(self):
        return self.user.username


class Delivery(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='deliverys')

    def __str__(self):
        return self.user.username
