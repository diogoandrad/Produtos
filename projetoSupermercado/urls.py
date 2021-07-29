from django.contrib import admin
from django.urls import path
from appProdutos.views import (home, 
    listProduto, createProduto, updateProduto, deleteProduto, 
    listCategoria, createCategoria, updateCategoria, deleteCategoria)

urlpatterns = [
    # Administrador
    path('admin/', admin.site.urls),

    # Página Inicial
    path('', home, name='home'),

    # Produtos
    path('produtos/', listProduto, name='produto_list'),
    path('produtos/create/', createProduto, name='produto_create'),
    path('produtos/update/<int:pk>', updateProduto, name='produto_update'),
    path('produtos/delete/<int:pk>', deleteProduto, name='produto_delete'),

    # Categorias
    path('categorias/', listCategoria, name='categoria_list'),
    path('categorias/create/', createCategoria, name='categoria_create'),
    path('categorias/update/<int:pk>', updateCategoria, name='categoria_update'),
    path('categorias/delete/<int:pk>', deleteCategoria, name='categoria_delete')
]