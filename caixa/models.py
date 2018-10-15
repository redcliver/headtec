from django.db import models
from django.utils import timezone

# Create your models here.
class caixa_geral(models.Model):
    OPERACAO = (
        ('1', 'Entrada'),
        ('2', 'Saida'),
    )
    id = models.AutoField(primary_key=True)
    valor_op = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    descricao_op = models.CharField(max_length=300, null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)
    op = models.CharField(max_length=1, choices=OPERACAO)
    
    def __str__(self):
        return self.descricao_op