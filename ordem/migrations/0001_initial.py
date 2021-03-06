# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-13 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('1', 'Em Aberto'), ('2', 'Finalizada')], max_length=1)),
                ('metodo', models.CharField(blank=True, choices=[('1', 'Dinheiro'), ('2', 'Cartao Debito'), ('3', 'Cartao Credito')], max_length=1, null=True)),
                ('data_abertura', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_fechamento', models.DateTimeField(blank=True, null=True)),
                ('desc', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cliente_ordem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
        ),
    ]
