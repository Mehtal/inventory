from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_seller = models.BooleanField('seller status', default=False)
    is_delivery = models.BooleanField('delivery status', default=False)


class Product(models.Model):
    name = models.CharField(max_length=20, unique=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = name = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name


class Variant(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey('Color', on_delete=models.CASCADE, default='')
    size = models.ManyToManyField('Size',)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.product.name}  {self.color.name}'


class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, )
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="senders")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recievers")
    quantity = models.IntegerField()
    trans_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{from_user} sent {to_user} {quantity} {product}'


class Order(models.Model):
    variant = variant = models.ForeignKey(Variant, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    buyer_name = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    observation = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone} has ordred {self.variant} in {self.location}'
