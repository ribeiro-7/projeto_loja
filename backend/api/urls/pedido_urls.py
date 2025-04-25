from django.urls import path
from api.views import pedido_views as views

urlpatterns = [
    path('adicionar/', views.addItemPedido, name='adicionar-pedido'),
    path('meuspedidos/', views.getMeusPedidos, name='meus-pedidos'),
    path('<str:pk>/revisoes/', views.criarRevisaoProduto, name='criar_revisao'),
    path('<str:pk>/', views.getPedidoPorId, name='pedido-id'),
    path('<str:pk>/pagar/', views.updatePedidoParaPago, name='pagamento'),
]
