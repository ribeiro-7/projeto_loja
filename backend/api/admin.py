from django.contrib import admin
from .models import *

admin.site.register(Produto)
admin.site.register(Revisao)
admin.site.register(ItemPedido)
admin.site.register(EnderecoDeEntrega)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        "user", "criadoEm", "precoFinal"
    ]

