from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^empresa', views.empresa),
    url(r'^produto', views.produto_view),
    url(r'^busca_produto', views.busca_produto),
    url(r'^editar_produto', views.editar_produto),
    url(r'^servico', views.servico),
    ]
