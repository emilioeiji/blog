from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from contas.models import Perfil


class Post(models.Model):
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    image_capa = models.ImageField(null=True, blank=True, upload_to="static/blog/img/")
    data_publicacao = models.DateField()
    tempo_leitura = models.CharField(max_length=2, default=30)

    def __str__(self):
        return self.titulo


class Tag(models.Model):
    nome = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return str(self.nome)

class Assunto(models.Model):
    nome = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return str(self.nome)

class Situacao(models.Model):
    nome = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, through='PostSituacao', through_fields=('situacao', 'post'))

    def __str__(self):
        return str(self.nome)

class PostSituacao(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    data = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ['post', 'situacao']

class Topico(models.Model):
    conteudo = RichTextField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.conteudo)

class Comentario(models.Model):
    texto = models.TextField(max_length=1024)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.texto)