# forms.py
from django import forms
from .models import MinhaImagem

class MinhaImagemForm(forms.ModelForm):
    class Meta:
        model = MinhaImagem
        fields = ['imagem']
