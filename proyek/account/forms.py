from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'form_control'
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class':'form_control'
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'form_control'
            }
        )
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class':'form_control'
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class':'form_control'
            }
        )
    )
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'form_control'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username','password1','password2','email','is_admin','is_staff')