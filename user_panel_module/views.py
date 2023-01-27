from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from user_panel_module.forms import EditUserForm, ChangePasswordUserForm


class UserPanelDashboard(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard.html'


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        form_edit = EditUserForm(instance=current_user)
        context = {
            'form_edit': form_edit
        }
        return render(request, 'user_panel_module/edit_user.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        form_edit = EditUserForm(request.POST, request.FILES, instance=current_user)
        if form_edit.is_valid():
            form_edit.save(commit=True)
        context = {
            'form_edit': form_edit
        }
        return render(request, 'user_panel_module/edit_user.html', context)


class ChangePasswordUser(View):
    def get(self, request):
        form_change = ChangePasswordUserForm()
        context = {
            'change_pass': form_change
        }

        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request: HttpRequest):
        form_change = ChangePasswordUserForm(request.POST)
        if form_change.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            old_pass = form_change.cleaned_data.get('old_password')
            if current_user.check_password(old_pass):
                new_pass = form_change.cleaned_data.get('password')
                current_user.set_password(new_pass)
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form_change.add_error('old_password', 'رمز عبور شما اشتباه است ')
        context = {
            'change_pass': form_change

        }
        return render(request, 'user_panel_module/change_password_page.html', context)


def user_panel_menu_partial(request: HttpRequest):
    return render(request, 'componet/user_panel_partial.html')
