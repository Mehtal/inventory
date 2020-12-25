from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from core.models import User
from .forms import SellerSignUpForm
from django.contrib.auth import login
# Create your views here.


class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
