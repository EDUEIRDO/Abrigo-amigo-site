from django.db import models

class Animais(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    raça = models.TextField(max_length=255)
    gênero = models.TextField(max_length=255)
#    imagem = models.ImageField(upload_to='projeto_abrigo_amigo/app_abrigo_amigo/fotos/', width_field=None, height_field=None, max_length=100)

class MinhaImagem(models.Model):
    imagem = models.ImageField(upload_to='imagens/')