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
    
