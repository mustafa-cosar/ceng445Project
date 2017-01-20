from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError

class UserRegister(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    email = forms.CharField(label="Email", max_length=70)
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput)

    class Meta:
        model=User

    def clean_username(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise ValidationError(_("The username already exists. Please try another one."))

    def clean_email(self):
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except Exception as e:
            return self.cleaned_data['email']
        raise ValidationError(_("The username already exists. Please try another one."))

class UserLogin(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput)
    class Meta:
        model=User
