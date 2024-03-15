from django import forms
from .models import *
class Animal_Form(forms.ModelForm):
    class Meta:
        model = Animais
        fields = ['foto']
