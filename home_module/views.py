from django.shortcuts import render

# Create your views here.
from account_module.models import User
from home_module.models import SiteSetting
from site_module.models import Slider


def index_page(request):
    slider = Slider.objects.filter(is_active=True)
    context = {
        'sliders': slider

    }
    return render(request, 'home_module/index_page.html', context)


def site_header_partial(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    uaer: User = User.objects.filter(is_active=True)
    context = {
        'setting': setting,
        'user': uaer
    }
    return render(request, 'shared/header_partial.html', context)


def site_footer_partial(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'setting': setting

    }
    return render(request, 'shared/footer_partial.html', context)


def about_us(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'setting': setting

    }
    return render(request, 'home_module/about_us.html', context)
