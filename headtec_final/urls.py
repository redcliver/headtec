"""
Definition of urls for headtec_final.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
from django.contrib.auth.views import login

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^login/', login, {'template_name': 'home/login.html'}),
    url(r'^$', include('home.urls')),
    url(r'^controle/', include('controle.urls')),
    url(r'^contas/', include('contas.urls')),
    url(r'^cliente/', include('cliente.urls')),
    url(r'^caixa/', include('caixa.urls')),
    url(r'^ordem/', include('ordem.urls')),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
