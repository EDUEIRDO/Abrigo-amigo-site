from django.shortcuts import render, redirect
from .models import Animais
from .forms import AnimaisForm


# Create your views here.
def home(request):
    novo_animal = Animais()
    novo_animal.nome = request.POST.get('nome')
    novo_animal.idade = request.POST.get('idade')
    novo_animal.raça = request.POST.get('raça')
    novo_animal.gênero = request.POST.get('gênero')
    novo_animal.imagem = request.POST.get('imagem')
    animal ={
        'animais': Animais.objects.all()
    }
    return render(request, 'index.html', animal)

def banco(request):
    return render(request, 'admin/db.html')

def form_info(request):
    if request.method == 'POST':
        form = AnimaisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = AnimaisForm()
    return render(request, 'db.html', {'form': form})

def sucesso(request):
    return render(request, 'admin/cadastrados.html')


#def admin(request):
#    form = Animal_Form(request.POST, request.FILES)
#    if form.is_valid():
#        form.save()
#        return render(request, 'admin/cadastrados.html', {'form': form})

#def admin(request):
#    novo_animal = Animais()
#    novo_animal.nome = request.POST.get('nome')
#    novo_animal.idade = request.POST.get('idade')
#    novo_animal.raça = request.POST.get('raça')
#    novo_animal.gênero = request.POST.get('gênero')
#    novo_animal.imagem = request.POST.get('imagem')
#    novo_animal.save()

#    animal ={
#        'animais': Animais.objects.all()
#    }
#    return render(request, 'admin/cadastrados.html', animal)