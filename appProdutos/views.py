from django.shortcuts import render, redirect
from .models import Categoria, Produto
from .forms import CategoriaForm, ProdutoForm
import datetime

def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    return render(request, 'home.html', data)

# Gerenciamento dos Produtos

def listProduto(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/list.html', {'produtos': produtos})

def createProduto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('produto_list')

    return render(request, 'produto/form.html', {'form': form})

def updateProduto(request, pk):
    data = {}
    produto = Produto.objects.get(pk=pk)
    data['produto'] = produto
    form = ProdutoForm(request.POST or None, instance=produto)
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('produto_list')

    return render(request, 'produto/form.html', data)

def deleteProduto(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    return redirect('produto_list')

# Gerenciamento das Categorias

def listCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/list.html', {'categorias': categorias})

def createCategoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('categoria_list')

    return render(request, 'categoria/form.html', {'form': form})

def updateCategoria(request, pk):
    data = {}
    categoria = Categoria.objects.get(pk=pk)
    data['categoria'] = categoria
    form = CategoriaForm(request.POST or None, instance=categoria)
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('categoria_list')

    return render(request, 'categoria/form.html', data)

def deleteCategoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    categoria.delete()
    return redirect('categoria_list')