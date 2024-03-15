from django.db import models

class Animais(models.Model):
    #id_animal = models.AutoField(primary_key=True)
#    imagem = models.ImageField(upload_to='projeto_abrigo_amigo\app_abrigo_amigo\templates\admin\imgs')
    #nome = models.TextField(max_length=255)
    #idade = models.IntegerField()
    #raça = models.TextField(max_length=255)
    #gênero = models.TextField(max_length=255)
    foto = models.ImageField(upload_to='fotos/')
