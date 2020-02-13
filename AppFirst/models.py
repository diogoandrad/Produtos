from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    dt_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Transacao(models.Model):
    data = models.DateTimeField()
    produto = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null= True, blank=True)

    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self):
        return self.produto
