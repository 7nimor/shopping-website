from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product_categories_list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product_brand_partial'),
    path('<slug:slug>', views.product_detail, name='product-detail'),
]
