from django.db import models

class Clientes(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.CharField('Endereço', max_length=100)
    idade = models.IntegerField('Idade')

    def __str__(self):
        return self.nome