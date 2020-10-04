from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from AppOne.models import UserProfile


class UserForm(forms.ModelForm):

    password= forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model= User
        fields=['username','email','password']


class Usr_Profile_Form(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('portfolio_site','picture')

        #both of the fields have to check with the variables created in models