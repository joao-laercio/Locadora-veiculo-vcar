from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Carro(models.Model):
    placa = models.CharField('Placa', max_length=10)
    marca = models.CharField('Marca', max_length=200)
    ano = models.CharField('Ano', max_length=4)
    modelo = models.CharField('Ano', max_length=20)
    img = models.ImageField("Imagem", upload_to='imagens', null=True, blank=True)
    data_compra = models.DateField('Data de compra')
    
    def __str__(self):
        return "{}" - "{}".format(self.marca, self.modelo )
        
class Cliente(models.Model):
    cpf = models.CharField('Cpf', max_length=11)
    nome = models.CharField('Nome', max_length=50)
    data_nacimento = models.DateField('Data de nascimento')
    endereco = models.CharField('Ano', max_length=200)
    
    def __str__(self):
        return "{}" - "{}".format(self.cpf, self.nome)
   
    
class Aluguel(models.Model):

    codigo = models.CharField("Codigo", max_length=100)
    data_aluguel = models.DateField("Data de aluguel")
    data_devolucao = models.DateField("Data de devolução")
    valor = models.DecimalField("Valor", max_digits=15, decimal_places=2)
    devolucao = models.BooleanField("Devolvido")
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, related_name='cliente_alugueis', verbose_name="Cliente")
    carro = models.ForeignKey(Carro, on_delete=models.DO_NOTHING, related_name='carro_alugueis', verbose_name="Carro") 

    def __str__(self):
        return "{} - {} - {}".format(self.codigo, self.cliente.nome, self.carro.modelo)

        