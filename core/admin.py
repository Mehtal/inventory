from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Variant, Color, Size, Transaction, Order

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Transaction)
admin.site.register(Order)
