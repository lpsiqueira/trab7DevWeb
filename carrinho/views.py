from django.shortcuts import render, redirect, HttpResponse
from .models import Carrinho
from appsite.models import Projeto
from .forms import RemoveItem

# Create your views here.
def carrinho(request):
    if request.method == 'POST':
        form = RemoveItem(request.POST)
        if form.is_valid():
            i = Carrinho.objects.get(pk=form.cleaned_data['item_id'])
            i.delete()
    else:
        form = RemoveItem()

    itens = []
    context = {'form': form}
    try:
        query = Carrinho.objects.filter(user=request.user)
        for item in query:
            #proj = Projeto.objects.get(pk=item.projeto)
            itens.append({'nome': item.projeto.nomeProjeto, 'qtd': item.quantidade, 'id': item.id})        
        context['itens'] = itens        

    except Carrinho.DoesNotExist:
        pass

    return render(request, 'carrinho/carrinho.html', context)

def adiciona(idProjeto, usuario):
    try:
        item = Carrinho.objects.get(user=usuario, projeto=idProjeto)
        item.quantidade += 1
        response = 'carrinho alterado'
    
    except Carrinho.DoesNotExist:
        proj = Projeto.objects.get(pk=idProjeto)
        item = Carrinho(projeto=proj, user=usuario, quantidade=1)
        response = 'item adicionado ao carrinho'
        
    item.save()
    #return HttpResponse(response)
    return redirect('appsite:busca')