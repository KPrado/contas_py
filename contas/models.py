from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateField(auto_now_add=True)

class Transacao(models.Model):
    data = models.DateField(auto_now_add=True)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categ = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField()