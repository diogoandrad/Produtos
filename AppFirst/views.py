from django.shortcuts import render, redirect
from .models import Transacao
from .forms import TransacaoForm
import datetime

def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['crud'] = ['Create', 'Read', 'Update','Delete']
    return render(request, 'home.html', data)

def lista(request):
    transacoes = Transacao.objects.all()
    return render(request, 'lista.html', {'transacoes': transacoes})

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    return render(request, 'form.html', {'form': form})

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    data['transacao'] = transacao
    form = TransacaoForm(request.POST or None, instance=transacao)
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    return render(request, 'form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_lista')
