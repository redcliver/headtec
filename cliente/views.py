from django.shortcuts import render
from .models import cliente

# Create your views here.
def cliente_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            name = request.POST.get('name')
            tel = request.POST.get('tel')
            cel = request.POST.get('cel')
            mail = request.POST.get('mail')
            novo_cliente = cliente(nome=name, telefone=tel, celular=cel, email=mail)
            novo_cliente.save()
            return render(request, 'cliente.html', {'title':'Clientes '})
        return render(request, 'cliente.html', {'title':'Clientes'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def busca_cliente(request):
    if request.user.is_authenticated():
        clientes = cliente.objects.all().order_by('nome')
        if request.method == 'GET' and request.GET.get('cliente_id') != None:
            cliente_id = request.GET.get('cliente_id')
            cliente_obj = cliente.objects.filter(id=cliente_id).get()
            return render(request, 'edita_cliente.html', {'title':'Editar Cliente', 'cliente_obj':cliente_obj})
        return render(request, 'busca_cliente.html', {'title':'Busca Clientes', 'clientes':clientes})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def edita_cliente(request):
    if request.user.is_authenticated():
        if request.method == 'GET' and request.GET.get('cliente_id') != None:
            cli_id = request.GET.get('cliente_id')
            cli_obj = cliente.objects.filter(id=cli_id).get()
            return render(request, 'edita_cliente.html', {'title':'Editar Cliente', 'cliente_obj':cli_obj})
        elif request.method == 'POST' and request.POST.get('id') != None:
            cliente_id = request.POST.get('id')
            cliente_obj = cliente.objects.filter(id=cliente_id).get()
            cliente_nome = request.POST.get('name')
            cliente_tel = request.POST.get('tel')
            cliente_cel = request.POST.get('cel')
            cliente_email = request.POST.get('mail')
            cliente_obj.nome = cliente_nome
            cliente_obj.telefone = cliente_tel
            cliente_obj.celular = cliente_cel
            cliente_obj.email = cliente_email
            cliente_obj.save()
            clientes = cliente.objects.all().order_by('nome')
            return render(request, 'busca_cliente.html', {'title':'Buscar cliente', 'clientes':clientes})
        
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})