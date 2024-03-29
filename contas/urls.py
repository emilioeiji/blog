from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.criar_conta, name='criar_conta'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


htmlx_urlpatterns = [
    path('contas/htmx_valida_username', views.htmx_valida_username, name='htmx_valida_username'),
    path('contas/htmx_valida_senha', views.htmx_valida_senha, name='htmx_valida_senha'),
    path('contas/htmx_valida_email', views.htmx_valida_email, name='htmx_valida_email'),
]

urlpatterns += htmlx_urlpatterns