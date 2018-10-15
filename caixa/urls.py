from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^caixa', views.caixa),
    ]
