from django.shortcuts import render
from product_module.models import Product
# Create your views here.


def add_to_order(request):
    product_id=request.GET.get('product_id')
    count=request.GET.get('count')
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            pass
