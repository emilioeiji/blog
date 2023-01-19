from django.urls import path
from . import views


urlpatterns = [
    path('', views.criar_conta, name='criar_conta'),
]


htmlx_urlpatterns = [
    path('contas/htmx_valida_username', views.htmx_valida_username, name='htmx_valida_username'),
    path('contas/htmx_valida_senha', views.htmx_valida_senha, name='htmx_valida_senha'),
]

urlpatterns += htmlx_urlpatterns