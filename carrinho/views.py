from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import Carrinho
from appsite.models import Projeto
from .forms import RemoveItem

# Create your views here.
def carrinho(request):
    if request.method == 'POST':
        form = RemoveItem(request.POST, auto_id=False)
        form.is_valid()

        if request.POST.get('remover') == 'true':
            i = Carrinho.objects.get(pk=int(request.POST.get('id')))
            i.delete()
            return HttpResponse()

        else:
            quantidade = request.POST.get('quantidade')
            if quantidade != '':
                idQuantidade = request.POST.get('id')
                itemQtd = Carrinho.objects.get(pk=idQuantidade)
                itemQtd.quantidade = quantidade
                itemQtd.save()
                itemQtd = Carrinho.objects.get(pk=idQuantidade)
                quantidade = itemQtd.quantidade
                saida = {'quantidade': quantidade}
                return JsonResponse(saida)

    else:
        form = RemoveItem(auto_id=False)

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