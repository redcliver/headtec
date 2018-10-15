from django.shortcuts import render
from .models import conta
from caixa.models import caixa_geral
from cliente.models import cliente
# Create your views here.
def contas_pagar(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name'):
            name = request.POST.get('name')
            valor = request.POST.get('valor')
            desc = request.POST.get('desc')
            data = request.POST.get('date')
            nova_conta = conta(nome=name, valor=valor, descricao=desc, data_vencimento=data, estado=1)
            nova_conta.save()
            return render(request, 'contas_pagar.html', {'title':'Contas a pagar '})
        return render(request, 'contas_pagar.html', {'title':'Contas a pagar'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def busca_contas_pagar(request):
    if request.user.is_authenticated():
        contas = conta.objects.all().filter(estado=1).order_by('data_vencimento')
        if request.method == 'GET' and request.GET.get('cliente_id') != None:
            cliente_id = request.GET.get('cliente_id')
            cliente_obj = cliente.objects.filter(id=cliente_id).get()
            return render(request, 'busca_contas_pagar.html', {'title':'Buscar conta', 'cliente_obj':cliente_obj})
        return render(request, 'busca_contas_pagar.html', {'title':'Buscar conta', 'contas':contas})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def pagar_contas_pagar(request):
    if request.user.is_authenticated():
        contas = conta.objects.all().filter(estado=1).order_by('data_vencimento')
        if request.method == 'GET' and request.GET.get('cliente_id') != None:
            cliente_id = request.GET.get('cliente_id')
            cliente_obj = cliente.objects.filter(id=cliente_id).get()
            return render(request, 'pagar_contas_pagar.html', {'title':'Editar Cliente', 'cliente_obj':cliente_obj})
        return render(request, 'pagar_contas_pagar.html', {'title':'Pagar Conta', 'contas':contas})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def contas_receber(request):
    if request.user.is_authenticated():
        return render(request, 'contas_receber.html', {'title':'Contas a receber'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})