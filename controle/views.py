from django.shortcuts import render
from django.contrib import messages
from decimal import Decimal
from .models import produto

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return render(request, 'controle/home.html', {'title':'Home'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def empresa(request):
    if request.user.is_authenticated():
        return render(request, 'controle/empresa.html', {'title':'Empresa'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})




def produto_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name') != None:
            nome = request.POST.get('name')
            v_compra = request.POST.get('valor_comp')
            v_venda = request.POST.get('valor_vend')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            novo_produto = produto(nome=nome, valor_venda=v_venda, valor_compra=v_compra, quantidade=qnt, qnt_min=qnt_min)
            novo_produto.save()
            return render(request, 'controle/produto.html', {'title':'Produtos'})
        return render(request, 'controle/produto.html', {'title':'Produtos'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def busca_produto(request):
    if request.user.is_authenticated():
        prods = produto.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('prod_id') != None:
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            return render(request, 'controle/visualizar_produto.html', {'title':'Buscar Produtos', 'produto_obj':produto_obj})
        return render(request, 'controle/busca_produto.html', {'title':'Buscar Produtos', 'prods':prods})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_produto(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            prod_id = request.GET.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            return render(request, 'controle/editar_produto.html', {'title':'Editar Produtos', 'produto_obj':produto_obj})
        elif request.method == 'POST' and request.POST.get('prod_id') != None and request.POST.get('valor_vend') != None and request.POST.get('valor_comp') != None and request.POST.get('valor_vend') != "" and request.POST.get('valor_comp') != "":
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            nome = request.POST.get('name')
            v_compra = request.POST.get('valor_comp')
            v_venda = request.POST.get('valor_vend')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = nome
            produto_obj.valor_compra = v_compra
            produto_obj.valor_venda = v_venda
            produto_obj.quantidade = qnt
            produto_obj.qnt_min = qnt_min
            produto_obj.save()
            prods = produto.objects.all().order_by('nome')
            return render(request, 'controle/busca_produto.html', {'title':'Editar Produtos', 'prods':prods})
        elif request.method == 'POST' and request.POST.get('prod_id') != None and request.POST.get('valor_vend') != "" and request.POST.get('valor_comp') != "" :
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            nome = request.POST.get('name')
            v_compra = request.POST.get('valor_comp')
            v_venda = request.POST.get('valor_vend')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = nome
            produto_obj.valor_compra = v_compra
            produto_obj.valor_venda = v_venda
            produto_obj.quantidade = qnt
            produto_obj.qnt_min = qnt_min
            produto_obj.save()
            prods = produto.objects.all().order_by('nome')
            return render(request, 'controle/busca_produto.html', {'title':'Editar Produtos', 'prods':prods})
        elif request.method == 'POST' and request.POST.get('prod_id') != None and request.POST.get('valor_vend') == None and request.POST.get('valor_comp') != None:
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            nome = request.POST.get('name')
            v_compra = request.POST.get('valor_comp')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = nome
            produto_obj.valor_compra = v_compra
            produto_obj.quantidade = qnt
            produto_obj.qnt_min = qnt_min
            produto_obj.save()
            prods = produto.objects.all().order_by('nome')
            return render(request, 'controle/busca_produto.html', {'title':'Editar Produtos', 'prods':prods})
        elif request.method == 'POST' and request.POST.get('prod_id') != None and request.POST.get('valor_vend') == "" and request.POST.get('valor_comp') != "":
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            nome = request.POST.get('name')
            v_compra = request.POST.get('valor_comp')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = nome
            produto_obj.valor_compra = v_compra
            produto_obj.quantidade = qnt
            produto_obj.qnt_min = qnt_min
            produto_obj.save()
            prods = produto.objects.all().order_by('nome')
            return render(request, 'controle/busca_produto.html', {'title':'Editar Produtos', 'prods':prods})
        elif request.method == 'POST' and request.POST.get('prod_id') != None and request.POST.get('valor_vend') != None and request.POST.get('valor_comp') == None:
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            nome = request.POST.get('name')
            v_venda = request.POST.get('valor_vend')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = nome
            produto_obj.valor_venda = v_venda
            produto_obj.quantidade = qnt
            produto_obj.qnt_min = qnt_min
            produto_obj.save()
            prods = produto.objects.all().order_by('nome')
            return render(request, 'controle/busca_produto.html', {'title':'Editar Produtos', 'prods':prods})
        elif request.method == 'POST' and request.POST.get('prod_id') != None and request.POST.get('valor_vend') != "" and request.POST.get('valor_comp') == "":
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            nome = request.POST.get('name')
            v_venda = request.POST.get('valor_vend')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = nome
            produto_obj.valor_venda = v_venda
            produto_obj.quantidade = qnt
            produto_obj.qnt_min = qnt_min
            produto_obj.save()
            prods = produto.objects.all().order_by('nome')
            return render(request, 'controle/busca_produto.html', {'title':'Editar Produtos', 'prods':prods})
        elif request.method == 'POST' and request.POST.get('prod_id') != None and request.POST.get('valor_vend') == None and request.POST.get('valor_comp') == None:
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            nome = request.POST.get('name')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = nome
            produto_obj.quantidade = qnt
            produto_obj.qnt_min = qnt_min
            produto_obj.save()
            prods = produto.objects.all().order_by('nome')
            return render(request, 'controle/busca_produto.html', {'title':'Editar Produtos', 'prods':prods})
        elif request.method == 'POST' and request.POST.get('prod_id') != None and request.POST.get('valor_vend') == "" and request.POST.get('valor_comp') == "":
            prod_id = request.POST.get('prod_id')
            produto_obj = produto.objects.filter(id=prod_id).get()
            nome = request.POST.get('name')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = nome
            produto_obj.quantidade = qnt
            produto_obj.qnt_min = qnt_min
            produto_obj.save()
            prods = produto.objects.all().order_by('nome')
            return render(request, 'controle/busca_produto.html', {'title':'Editar Produtos', 'prods':prods})
        return render(request, 'controle/editar_produto.html', {'title':'Editar Produtos', 'produto_obj':produto_obj})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def servico(request):
    if request.user.is_authenticated():
        return render(request, 'controle/servico.html', {'title':'Servicos'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

