from django.db import models
from appsite.models import Projeto, Language
from django.contrib.auth.models import User
# Create your models here.

class Carrinho(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
