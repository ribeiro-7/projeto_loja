from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH

class Produto(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    imagem = models.ImageField(null=True, blank=True, default= "/images/placeholder.png", upload_to="images/")
    marca = models.CharField(max_length=200, null=True, blank=True)
    categoria = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    avaliacao = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    numAnalise = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    contagemEmEstoque = models.IntegerField(null=True, blank=True, default=0)
    criadoEm = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.nome +  " | " + self.marca + " | " + str(self.preco)
    
class Revisao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    avaliacao = models.IntegerField(null=True, blank=True, default=0)
    comentario = models.TextField(null=True, blank=True)
    criadoEm = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.avaliacao)

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    metodoDePagamento = models.CharField(max_length=200, null=True, blank=True)
    precoImposto = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    precoFrete = models.DecimalField(mmax_digits=12, decimal_places=2, null=True, blank=True)
    precoFinal = models.DecimalField(mmax_digits=12, decimal_places=2, null=True, blank=True)
    pagamentoConcluido = models.BooleanField(default=False)
    pagoEm = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    envioFeito = models.BooleanField(default=False)
    enviadoEm = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    criadoEm = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.criadoEm)

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    qtd = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    imagem = models.CharField(max_length=200,null=True,blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.nome)
    
class EnderecoDeEntrega(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=200, null=True, blank=True)
    pais = models.CharField(max_length=200, null=True, blank=True)
    precoFrete = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.endereco)