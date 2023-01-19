from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', include('autenticacao.urls')),
    path('contas/', include('contas.urls')),
    path('contato/', include('contato.urls')),
    path('cursos/', include('cursos.urls')),
    path('bootstrap/', include('exemplos.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)