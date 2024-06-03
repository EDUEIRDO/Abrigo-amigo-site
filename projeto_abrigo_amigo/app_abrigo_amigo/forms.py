from django import forms
from .models import Animais

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animais
        fields = ['nome', 'idade', 'raça', 'gênero', 'tipo', 'photo']

