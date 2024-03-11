from django.shortcuts import render
from .models import Animais

# Create your views here.
def home(request):
#    animais = Animais.objects.all().order_by('nome')
    return render(request, 'index.html')

def banco(request):
    return render(request, 'admin/db.html')

def admin(request):
    novo_animal = Animais()
#    novo_animal.foto = request.POST.get('foto')
    novo_animal.nome = request.POST.get('nome')
    novo_animal.idade = request.POST.get('idade')
    novo_animal.raça = request.POST.get('raça')
    novo_animal.gênero = request.POST.get('gênero')
    novo_animal.save()

    animal ={
        'animais': Animais.objects.all()
    }
    return render(request, 'admin/cadastrados.html', animal)