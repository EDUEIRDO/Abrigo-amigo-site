from django.urls import path
from app_abrigo_amigo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.banco, name='banco'),
    path('admin/cadastrados/', views.admin, name='listagem_animais'),
    path('cachorros/', views.dogs_page, name='dogs_page'),
    path('gatos/', views.cats_page, name='cats_page'),
    path('animal/', views.teste, name='teste'),
]