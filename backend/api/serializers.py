from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'nome', 'isAdmin']

    def get_id(self, obj):
        return obj.id
    
    def get_isAdmin(self, obj):
        #verifica se é admin ou usuário normal
        return obj.is_staff
    
    def get_nome(self, obj):
        #se o nome estiver em branco, atribui o email ao nome
        nome = obj.first_name
        if nome == "":
            nome = obj.email
        return nome
    
class UserSerializerComToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'nome', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    
class RevisaoSerializer(serializers.Serializer):
    class Meta:
        model = Revisao
        fields = '__all__'

class ProdutoSerializer(serializers.Serializer):
    revisoes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Produto
        fields = '__all__'

    def get_revisoes(self, obj):
        revisoes = obj.revisao_set.all()
        serializer = RevisaoSerializer(revisoes, many=True)
        return serializer.data
    
class EnderecoDeEntregaSerializer(serializers.Serializer):
    class Meta:
        model = EnderecoDeEntrega
        fields = '__all__'

class ItemPedidoSerializer(serializers.Serializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'

class PedidoSerializer(serializers.Serializer):
    itensPedidos = serializers.SerializerMethodField(read_only=True)
    enderecoDeEntrega = serializers.SerializerMethodField(read_only=True)
    User = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def get_itensPedidos(self, obj):
        itens = obj.itemPedido_set.all()
        serializer = ItemPedidoSerializer(itens, many=True)
        return serializer.data
    
    def get_enderecoDeEntrega(self, obj):
        try:
            endereco = EnderecoDeEntregaSerializer(obj.enderecoDeEntrega, many=False).data
        except:
            endereco = False
        return endereco
    
    def get_user(self, obj):
        itens = obj.user
        serializer = UserSerializer(itens, many=True)
        return serializer.data