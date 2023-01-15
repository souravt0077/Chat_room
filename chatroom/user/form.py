from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class myUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','avatar','password1','password2']


class updateUserForm(myUserForm):
    password1=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'New password'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Confirm New password'}))

    class Meta:
        model=User
        fields=['username','email','avatar','password1','password2']