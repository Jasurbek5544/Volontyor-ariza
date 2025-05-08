from django import forms
from .models import Application, Direction, Viloyat, Tuman
import re
from django.contrib.auth.models import User

class ApplicationForm(forms.ModelForm):
    viloyat = forms.ModelChoiceField(
        queryset=Viloyat.objects.all(),
        empty_label="Viloyatni tanlang",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'viloyat-select'})
    )
    tuman = forms.ModelChoiceField(
        queryset=Tuman.objects.none(),
        empty_label="Tumanni tanlang",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'tuman-select'})
    )
    yashash_joyi = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Yashash joyingizni kiriting'})
    )
    
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'father_name', 'viloyat', 'tuman', 
                 'yashash_joyi', 'phone', 'direction', 'passport_image', 'selfi_image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangizni kiriting'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Otangizning ismini kiriting'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingizni kiriting'}),
            'direction': forms.Select(attrs={'class': 'form-control'}),
            'passport_image': forms.FileInput(attrs={'class': 'form-control'}),
            'selfi_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'viloyat' in self.data:
            try:
                viloyat_id = int(self.data.get('viloyat'))
                self.fields['tuman'].queryset = Tuman.objects.filter(viloyat_id=viloyat_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['tuman'].queryset = self.instance.viloyat.tumanlar.all()

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
