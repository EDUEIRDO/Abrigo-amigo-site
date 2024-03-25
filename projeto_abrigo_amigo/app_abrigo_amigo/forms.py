from django import forms
from .models import FormAnimal

#class AnimaisForm(forms.ModelForm):
#    class Meta:
#        model = Animais
#        fields = ['nome', 'idade', 'raça', 'gênero', 'imagem']
#

class AdotarForm(forms.ModelForm):
    class Meta:
        model = FormAnimal
        fields = ['nome', 'idade']