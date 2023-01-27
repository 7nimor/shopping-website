from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, ProductCategory, ProductBrand, BannerModel


# Create your views here.

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_module/product_list.html', {
#         'products': products,
#     })


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['banners'] = BannerModel.objects.filter(is_active=True,
                                                        position__iexact=BannerModel.BannerPosition.product_list)
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        request: HttpRequest = self.request
        brand_name = self.kwargs.get('brand')

        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        return query


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    banner=BannerModel.objects.filter(is_active=True,position__iexact=BannerModel.BannerPosition.product_detail)
    return render(request, 'product_module/product_detail.html', {
        'product': product,
        'banners':banner
    })


def product_category_partial(request: HttpRequest):
    product_category = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'product_category': product_category
    }
    return render(request, 'componet/product_category_partial.html', context)


def product_brand_partial(request: HttpRequest):
    brand = ProductBrand.objects.annotate(products_cont=Count('product')).filter(is_active=True)
    context = {
        'brand': brand
    }
    return render(request, 'componet/product_brand_partial.html', context)
