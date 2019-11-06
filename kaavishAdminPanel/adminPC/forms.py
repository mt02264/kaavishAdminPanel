from django.db import models
from django import forms
from .models import *


cssFormTextClass = forms.TextInput(
        attrs={
            "class":"form-control",
        }
    )

cssFormPasswordClass = forms.TextInput(
    attrs={
        "class":"form-control",
        "type":"password",
    }
)


class loginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=cssFormTextClass)
    password = forms.CharField(max_length=20, widget=cssFormPasswordClass)
