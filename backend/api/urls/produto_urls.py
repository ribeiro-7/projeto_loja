from django.urls import path
from api.views import produto_views as views

urlpatterns = [
    path('', views.getProdutos, name='produtos'),
    path('<str:pk>/revisoes/', views.criarRevisaoProduto, name='criar_revisao'),
    path('top/', views.getTopProdutos, name='top_produtos'),
    path('<str:pk>/', views.getProduto, name='produto'),
]
