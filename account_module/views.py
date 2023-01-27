from django.contrib.auth import login, logout
from utils.email_sercise import send_email
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.utils.crypto import get_random_string
from account_module.forms import RegisterForm, LoginForm, ForgetForm, ResetForm
from account_module.models import User


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email_user = register_form.cleaned_data.get('email')
            password_user = register_form.cleaned_data.get('password')
            if User.objects.filter(email=email_user).exists():
                register_form.add_error('email', 'کاربر قبلا در سایت ثبت نام کرده است')
            else:
                new_user = User(email=email_user, email_active_code=get_random_string(72))
                new_user.set_password(password_user)
                new_user.username = email_user
                new_user.is_active = False
                new_user.save()
                send_email('فعال سازی حساب کاربری', new_user.email, {'new_user': new_user}, 'emails/active_email.html')

                return redirect(reverse('index'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            email_user = login_form.cleaned_data.get('email')
            password_user = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=email_user).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'شما در سایت ثبت نام نکرده اید')
                is_password_correct = user.check_password(password_user)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('user_panel_dashboard'))

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)


class ActivateView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo:
                return redirect(reverse('login_page'))
            else:
                pass

        raise Http404


class ForgetPassword(View):
    def get(self, request):
        forget_form = ForgetForm()
        context = {
            'forget_form': forget_form
        }

        return render(request, 'account_module/forget_password.html', context)

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email_user = forget_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=email_user).first()
            if user is not None:
                # todo:send email active code to user
                pass
        context = {
            'forget_form': forget_form
        }

        return render(request, 'account_module/forget_password.html', context)


class ResetPassword(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(email_active_code=active_code).first()
        if user is None:
            return redirect(reverse('index'))
        reset_form = ResetForm()
        context = {
            'reset_form': reset_form
        }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request, active_code):
        reset_form = ResetForm(request.POST)
        if reset_form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                return redirect(reverse('login_page'))
            new_pass = reset_form.cleaned_data.get('password')
            user.set_password(new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('index'))
        context = {
            'reset_form': reset_form
        }

        return render(request, 'account_module/reset_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('index'))
