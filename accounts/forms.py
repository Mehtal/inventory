from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.conf import settings
from core.models import User
from .models import Seller
from django.contrib.admin.widgets import AdminDateWidget


class SellerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        seller = Seller.objects.create(user=user)
        return user
