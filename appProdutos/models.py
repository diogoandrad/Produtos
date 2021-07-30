from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    dataValidade = models.DateField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null= True, blank=True)
    dt_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome