from django.contrib import admin

# Register your models here.
from .models import Delivery, Seller


admin.site.register(Seller)
admin.site.register(Delivery)
