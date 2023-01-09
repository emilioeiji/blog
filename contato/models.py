from django.db import models


class Contato(models.Model):
    assunto = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(max_length=1000)