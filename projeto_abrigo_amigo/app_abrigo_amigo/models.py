from django.db import models

class Animais(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    raça = models.TextField(max_length=255)
    gênero = models.TextField(max_length=255)
    tipo = models.TextField(max_length=5)

class RelatorioAdopção(models.Model):
    name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    idade = models.IntegerField()
    gênero = models.TextField(max_length=255)
    cpf = models.TextField(max_length=11)
    telefone = models.IntegerField()
    cep = models.TextField(max_length=255)
    logradouro = models.TextField(max_length=255)
    num_casa = models.IntegerField()
    bairro = models.TextField(max_length=255)
    cidade = models.TextField(max_length=255)
    uf = models.TextField(max_length=2)