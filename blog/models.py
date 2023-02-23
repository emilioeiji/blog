from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    resumo = RichTextField(null=True, blank=True)
    conteudo = RichTextUploadingField()
    image_capa = models.ImageField(null=True, blank=True, upload_to="static/blog/img/")
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Topico(models.Model):
    conteudo = RichTextUploadingField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
