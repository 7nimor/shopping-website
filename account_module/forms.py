from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(),
        label='ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='پسورد'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='تکرار پسورد'

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        return ValidationError('کلمه عبور با تکرار آن مغایرت دارد')


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(),
        label='ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='پسورد'
    )


class ForgetForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(),
        label='ایمیل'
    )


class ResetForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='پسورد'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='تکرار پسورد'

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        return ValidationError('کلمه عبور با تکرار آن مغایرت دارد')
