from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404, HttpResponse
from .models import Animais
from .forms import AnimalForm

# Create your views here.
def home(request):
    novo_animal = Animais()
    novo_animal.id_animal = request.POST.get('id_animal')
    novo_animal.nome = request.POST.get('nome')
    novo_animal.idade = request.POST.get('idade')
    novo_animal.raça = request.POST.get('raça')
    novo_animal.gênero = request.POST.get('gênero')
    novo_animal.tipo = request.POST.get('tipo')
    animal ={
        'animais': Animais.objects.all()
    }
    return render(request, 'index.html', animal)

def banco(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin/cadastrados.html')
    else:
        form = AnimalForm()
        return render(request, 'admin/db.html', {'form': form})

#def form_info(request):
#    if request.method == 'POST':
#        form = AnimaisForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('sucesso')
#    else:
#        form = AnimaisForm()
#    return render(request, 'db.html', {'form': form})

#def sucesso(request):
#    return render(request, 'admin/cadastrados.html')

#Teste de formulario para adoção.
#def FormularioTeste(request):
#    form = FormAnimal(request.POST, request.FILES)
#    if form.is_valid():
#        form.save()
#        return render(request, 'admin/teste.html', {'form': form})

#Admin padrão para salvar cadastros e exibir    
def admin(request):
    animais = Animais.objects.all()
    return render(request, 'admin/cadastrados.html', {'animais': animais})

#Ajustar o filtro para exibição de dados!
def dogs_page(request):
    novo_animal = Animais()
    novo_animal.nome = request.POST.get('nome')
    novo_animal.idade = request.POST.get('idade')
    novo_animal.raça = request.POST.get('raça')
    novo_animal.gênero = request.POST.get('gênero')
    novo_animal.tipo = request.POST.get('tipo')
    animal ={
        'animais': Animais.objects.filter(tipo='C')
    }
    return render(request, 'admin/dogs_page.html', animal)


def cats_page(request):
    novo_animal = Animais()
    novo_animal.id_animal = request.POST.get('id_animal')
    novo_animal.nome = request.POST.get('nome')
    novo_animal.idade = request.POST.get('idade')
    novo_animal.raça = request.POST.get('raça')
    novo_animal.gênero = request.POST.get('gênero')
    novo_animal.tipo = request.POST.get('tipo')
    animal ={
        'animais': Animais.objects.filter(tipo='G')
    }
    return render(request, 'admin/cats_page.html', animal)

def page_adote(request, id_animal):
    animal = get_object_or_404(Animais, pk=id_animal)
    return render(request, 'teste.html', {'animal': animal})

def doação(request):
    return render(request, 'admin/doação.html')

def Denuncia(request):
    return render(request,'admin/denuncias.html')