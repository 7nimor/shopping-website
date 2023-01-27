from django import forms

from contact_module.models import ContactUs


class ContactUsModel(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'title', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message'
            })
        }
