from django.db import models
from django.contrib.auth.models import User

class EquipamentoNDS(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    sala = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    informacoes = models.TextField()
    descricao = models.TextField()

class Emprestimo(models.Model):
    equipamento = models.ForeignKey(EquipamentoNDS, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
