from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from django.views import View
from .forms import  ContactUsModel


class ContactView(View):
    def get(self, request):
        form = ContactUsModel()
        context = {
            'contact_form': form
        }
        return render(request, 'contact_module/contact_us.html', context)

    def post(self, request):
        contact_form = ContactUsModel(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('index'))
        context = {
            'contact_form': contact_form
        }
        return render(request, 'contact_module/contact_us.html', context)
