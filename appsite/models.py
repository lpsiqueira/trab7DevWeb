from django.db import models
#from django.conf import settings
from projeto import settings

class Language(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    autor = models.CharField(max_length=20)
    nomeProjeto = models.CharField(max_length=20)
    linguagem = models.ManyToManyField('Language')

    def __str__(self):
        return self.nomeProjeto

    def linguagens(self):
        return "\n".join([i.nome for i in self.linguagem.all()])