from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about-us', views.about_us, name=  'about_us'),
]
