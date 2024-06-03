from django.urls import path
from app_abrigo_amigo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin, name='admin'),
    path('banco/', views.banco, name='banco'),
    path('excluir/<int:id_animal>/', views.excluir_animal, name='excluir_animal'),
    path('atualizar/<int:id_animal>/', views.atualizar_animal, name='atualizar_animal'),
    path('dogs/', views.dogs_page, name='dogs_page'),
    path('cats/', views.cats_page, name='cats_page'),
    path('adote/<int:id_animal>/', views.page_adote, name='page_adote'),
    path('doacao/', views.doação, name='doacao'),
    path('denuncia/', views.Denuncia, name='denuncia'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
