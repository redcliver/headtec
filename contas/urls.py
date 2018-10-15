from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^contas_pagar', views.contas_pagar),
    url(r'^busca_contas_pagar', views.busca_contas_pagar),
    url(r'^pagar_contas_pagar', views.pagar_contas_pagar),
    url(r'^contas_receber', views.contas_receber),
    ]