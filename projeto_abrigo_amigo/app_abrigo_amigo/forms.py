from django import forms
from .models import Animais, RelatorioAdopção

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animais
        fields = ['nome', 'idade', 'raça', 'gênero', 'tipo']

class AdoçãoForm(forms.ModelForm):
    class Meta:
        model = RelatorioAdopção
        fields = ['name', 'email', 'idade', 'gênero', 'cpf', 'telefone', 'cep', 'logradouro', 'num_casa', 'bairro', 'cidade', 'uf']