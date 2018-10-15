from django.shortcuts import render
from cliente.models import cliente

# Create your views here.
def ordem(request):
    if request.user.is_authenticated():
        clientes = cliente.objects.all().order_by('nome')
        return render(request, 'ordem.html', {'title':'Ordens', 'clientes':clientes})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})