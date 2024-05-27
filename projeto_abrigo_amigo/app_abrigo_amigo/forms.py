from django import forms
from .models import Animais, RelatorioAdopção

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animais
        fields = ['nome', 'idade', 'raça', 'gênero', 'tipo']

