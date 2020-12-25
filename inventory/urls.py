"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import ProductDetail, add_transaction, Home, add_order ,VariantDetail,OrderListView
from accounts.views import SellerSignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('product/transfer', add_transaction, name="trans"),
    path('product/order', add_order, name='addorder'),
    path('product/<int:pk>', ProductDetail.as_view(), name="product-detail"),
    path('variant/<int:pk>', VariantDetail.as_view(), name="variant-detail"),
    path('orders/', OrderListView.as_view(), name="order-list"),
    path('__debug__/', include(debug_toolbar.urls)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/seller', SellerSignUpView.as_view(), name="seller-signup"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
