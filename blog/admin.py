from django.contrib import admin
from .models import Post, Topico, Tag, Comentario, Situacao, PostSituacao


class TopicoInline(admin.TabularInline):
    model = Topico


class PostAdmin(admin.ModelAdmin):
    inlines = [
        TopicoInline
    ]
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Topico)
admin.site.register(Tag)
admin.site.register(Comentario)
admin.site.register(Situacao)
admin.site.register(PostSituacao)
