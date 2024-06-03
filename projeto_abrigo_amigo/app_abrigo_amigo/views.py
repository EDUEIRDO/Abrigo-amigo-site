from django.shortcuts import render, get_object_or_404, redirect
from .models import Animais
from .forms import AnimalForm

# View principal para exibir animais
def home(request):
    animal ={
        'animais': Animais.objects.all()
    }
    return render(request, 'index.html', animal)

# View para salvar novo animal
def banco(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = AnimalForm()
    return render(request, 'admin/db.html', {'form': form})


def admin(request):
    animais = Animais.objects.all()
    return render(request, 'admin/cadastrados.html', {'animais': animais})

# View para exibir apenas cães
def dogs_page(request):
    animais = Animais.objects.filter(tipo='C')
    return render(request, 'admin/dogs_page.html', {'animais': animais})

# View para exibir apenas gatos
def cats_page(request):
    animais = Animais.objects.filter(tipo='G')
    return render(request, 'admin/cats_page.html', {'animais': animais})

# View para exibir detalhes de um animal específico
def page_adote(request, id_animal):
    animal = get_object_or_404(Animais, pk=id_animal)
    return render(request, 'teste.html', {'animal': animal})

# View para exibir a página de doação
def doação(request):
    return render(request, 'admin/doação.html')

# View para exibir a página de denúncias
def Denuncia(request):
    return render(request, 'admin/denuncias.html')

# View para excluir um animal
def excluir_animal(request, id_animal):
    animal = get_object_or_404(Animais, id_animal=id_animal)
    if request.method == 'POST':
        animal.delete()
        return redirect('admin')
    return render(request, 'admin/confirmar_exclusão.html', {'animal': animal})
    
# View para atualizar um animal
def atualizar_animal(request, id_animal):
    animal = get_object_or_404(Animais, id_animal=id_animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = AnimalForm(instance=animal)
        return render(request, 'admin/atualizar_animal.html', {'form': form})
