from django.urls import path
from app_abrigo_amigo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.banco, name='banco'),
    path('admin/cadastrados/', views.form_info, name='listagem_animais'),
    
]