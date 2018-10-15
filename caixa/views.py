from django.shortcuts import render
from .models import caixa_geral
from contas.models import conta, conta_receber

# Create your views here.
def caixa(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
        except:
            caixa = caixa_geral(op=1, valor_op=0, descricao_op="Abertura", total=0)
            caixa.save()
        try:
            pag = 0
            for p in conta.objects.filter(estado=1).all():
                pag = pag + p.valor
        except:
            pag = 0
        return render(request, 'caixa.html', {'title':'Caixa', 'caixa':caixa, 'pagar':pag})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})