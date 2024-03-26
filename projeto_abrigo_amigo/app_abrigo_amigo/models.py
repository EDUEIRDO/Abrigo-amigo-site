from django.db import models

class Animais(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    raça = models.TextField(max_length=255)
    gênero = models.TextField(max_length=255)
    tipo = models.TextField(max_length=5)

