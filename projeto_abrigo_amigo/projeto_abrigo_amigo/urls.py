from django.urls import path
from app_abrigo_amigo import views

urlpatterns = [
#    path('', views.home, name='home'),
    path('', views.banco, name='banco'),
    path('cadastrados/', views.admin, name='listagem_animais')
]