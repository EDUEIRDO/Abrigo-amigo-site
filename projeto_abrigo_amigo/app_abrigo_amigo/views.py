from django.shortcuts import render
from .models import Animais

# Create your views here.
def home(request):
    animal = Animais.objects.first()
    return render(request, 'index.html', {'animal': animal})

def banco(request):
    return render(request, 'admin/db.html')

#def admin(request):
#    form = Animal_Form(request.POST, request.FILES)
#    if form.is_valid():
#        form.save()
#        return render(request, 'admin/cadastrados.html', {'form': form})

def admin(request):
    novo_animal = Animais()
    novo_animal.nome = request.POST.get('nome')
    novo_animal.idade = request.POST.get('idade')
    novo_animal.raça = request.POST.get('raça')
    novo_animal.gênero = request.POST.get('gênero')
    novo_animal.imagem = request.POST.get('imagem')
    novo_animal.save()

    animal ={
        'animais': Animais.objects.all()
    }
    return render(request, 'admin/cadastrados.html', animal)