from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cliente', views.cliente_view),
    url(r'^busca_cliente', views.busca_cliente),
    url(r'^edita_cliente', views.edita_cliente),
    ]
