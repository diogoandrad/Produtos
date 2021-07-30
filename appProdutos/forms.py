from django import forms
from .models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100, required=True)

    class Meta:
        model = Categoria
        fields = ['nome']

class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=200, required=True)
    dataValidade = forms.DateField(label='Data Validade', required=True, widget=forms.DateInput(attrs={'type':'date'}))
    valor = forms.DecimalField(label='Valor', required=True)
    categoria = forms.ModelChoiceField(label='Categoria', required=True, queryset=Categoria.objects.all())
    observacoes = forms.CharField(label='Observações', required=False, widget=forms.Textarea)

    class Meta:
        model = Produto
        fields = ['nome', 'dataValidade', 'valor', 'categoria', 'observacoes']