from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
import datetime

def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['crud'] = ['Create', 'Read', 'Update','Delete']
    return render(request, 'home.html', data)

def list(request):
    produtos = Produto.objects.all()
    return render(request, 'lista.html', {'produtos': produtos})

def create(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_list')

    return render(request, 'form.html', {'form': form})

def update(request, pk):
    data = {}
    produto = Produto.objects.get(pk=pk)
    data['produto'] = produto
    form = ProdutoForm(request.POST or None, instance=produto)
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('url_list')

    return render(request, 'form.html', data)

def delete(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    return redirect('url_list')
