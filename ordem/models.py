from django.db import models
from cliente.models import cliente
from django.utils import timezone


class ordens(models.Model):
    ESTADO = (
        ('1', 'Em Aberto'),
        ('2', 'Finalizada'),
    )
    METODO = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao Debito'),
        ('3', 'Cartao Credito'),
    )
    id = models.AutoField(primary_key=True)
    cliente_ordem = models.ForeignKey(cliente)
    estado = models.CharField(max_length=1, choices=ESTADO)
    metodo = models.CharField(max_length=1, choices=METODO, null=True, blank=True)
    data_abertura = models.DateTimeField(default=timezone.now)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    desc = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.id)
