from django import forms
from django.forms import fields, widgets
from.models import Register
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        widgets = {
        'password': forms.PasswordInput(),
        'confirm': forms.PasswordInput(),

    }
        fields = ["first_name","last_name","username","email","password","confirm"]
   
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar','profession']
