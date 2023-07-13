from django import forms

from app1.models import *

class user_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput()}

class profile_form(forms.ModelForm):
    class Meta:
        model=profile
        fields=['username']