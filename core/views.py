from django.shortcuts import render, redirect
from .models import Product, User, Variant, Transaction, Order, Size
# Create your views here.
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.decorators import login_required


@login_required
def Home(request):
    p = Variant.objects.filter(owner=request.user)
    context = {
        'variants': p
    }
    return render(request, 'home.html', context)


@login_required
def add_order(request):
    v = Variant.objects.get(id=request.POST.get('variant'))
    user = User.objects.get(username=request.POST.get('user'))
    buyer_name = request.POST.get('buyer_name')
    phone = request.POST.get('phone')
    location = request.POST.get('location')
    observation = request.POST.get('observation')
    q = request.POST.get('quantity')
    order = Order(variant=v, user=user, buyer_name=buyer_name, phone=phone, location=location, quantity=q, observation=observation)
    order.save()
    return redirect('order-list')


@login_required
def add_transaction(request):
    product = Product.objects.get(name=request.POST.get('product'))
    # vlist = Variant.objects.filter(product__id=product_id)
    v = Variant.objects.get(id=request.POST.get('variant'))
    q = request.POST.get('quantity')
    to_user = User.objects.get(id=request.POST.get('to_user'))
    from_user = request.user
    transaction = Transaction(product=product, variant=v, from_user=from_user, to_user=to_user, quantity=q)
    v.owner = to_user
    v.quantity = int(q)
    product.quantity -= v.quantity
    v.save()
    product.save()
    transaction.save()

    return render(request, 'transaction.html', {'transaction': transaction, 'product': product, 'variant': v, 'sender': from_user, 'reciever': to_user, 'quantity': q})


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['variants'] = Variant.objects.filter(product__id=self.object.id)
        context['users'] = User.objects.all()
        return context


class VariantDetail(DetailView):
    model = Variant
    template_name = 'variant_details.html'
    context_object_name = 'variant'

    def get_context_data(self, **kwargs):
        context = super(VariantDetail, self).get_context_data(**kwargs)
        context['sizes'] = Size.objects.filter(variant__id=self.object.id)
        context['users'] = User.objects.all()
        return context


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user)
        context['users'] = User.objects.all()
        return context
