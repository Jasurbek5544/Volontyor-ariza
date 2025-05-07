from django import forms
from .models import Application
import re
from django.contrib.auth.models import User

class ApplicationForm(forms.ModelForm):
    phone = forms.CharField(
        label="Telefon raqam",
        max_length=9,
        min_length=9,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '901234567',
            'pattern': r'\d{9}',
            'title': 'Telefon raqam 9 ta raqamdan iborat bo‘lishi kerak (masalan, 901234567)'
        })
    )

    class Meta:
        model = Application
        fields = [
            'first_name', 'last_name', 'middle_name', 'address', 'phone',
            'direction', 'passport_image', 'selfie_image'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismingiz'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familiyangiz'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Otasining ismi'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Yashash manzili'
            }),
            'direction': forms.Select(attrs={
                'class': 'form-control',
            }),
            'passport_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'selfie_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        if not re.match(r'^\d{9}$', phone):
            raise forms.ValidationError("Faqat 9 ta raqam kiriting (masalan, 901234567)")
        return '+998' + phone

class AdminCreateForm(forms.ModelForm):
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Parolni tasdiqlang", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parollar mos emas!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = True
        if commit:
            user.save()
        return user
