from django import forms
from django.contrib.auth.models import User



class Registrationform(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

class Loginform(forms.Form):
    username=forms.CharField(max_length=250)
    password=forms.CharField(max_length=250)