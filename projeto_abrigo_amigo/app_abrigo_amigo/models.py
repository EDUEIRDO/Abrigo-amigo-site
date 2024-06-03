from django.db import models

class Animais(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    raça = models.CharField(max_length=100)
    gênero = models.CharField(max_length=50, default='Desconhecido')
    tipo = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.nome
