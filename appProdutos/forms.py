from django.forms import ModelForm
from .models import Categoria, Produto

class CategoriaForm(ModelForm):
    
    class Meta:
        model = Categoria
        fields = ['nome']

class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'valor', 'categoria', 'observacoes', 'data']