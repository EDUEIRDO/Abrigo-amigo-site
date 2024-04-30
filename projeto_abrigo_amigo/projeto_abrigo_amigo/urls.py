from django.urls import path
from app_abrigo_amigo import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.banco, name='banco'),
    path('admin/cadastrados/', views.admin, name='listagem_animais'),
    path('cachorros/', views.dogs_page, name='dogs_page'),
    path('gatos/', views.cats_page, name='cats_page'),
    path('animal/<int:id_animal>/', views.page_adote, name='page_adote'),
    path('doação/', views.doação, name='Doação'),
    path('denuncia/', views.Denuncia, name='denuncias')
]