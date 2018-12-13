from django.shortcuts import render, redirect, HttpResponse
from .models import Carrinho
from appsite.models import Projeto

# Create your views here.
def carrinho(request):
    return render(request, 'carrinho/carrinho.html')

def adiciona(idProjeto, usuario):
    proj = Projeto.objects.get(pk=idProjeto)
    item = Carrinho(projeto=proj, user=usuario, quantidade=1)
    #item.save()
    return HttpResponse(idProjeto)
