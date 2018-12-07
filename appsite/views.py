from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import ProjetoForm, RemoveProdutoForm
from .models import Projeto, Language
#from appsite.models import Image

def teste(request):
    return HttpResponse("Servidor ativo")

def index(request):
    return render(request, 'appsite/index.html')

def signIn(request):
    return render(request, 'appsite/sign_in.html')

def signUp(request):
    #imagem = get_object_or_404(Image, pk=2)
    return render(request, 'appsite/sign_up.html')

def busca(request):
    projetos = Projeto.objects.all()
    return render(request, 'appsite/busca.html', {'projetos': projetos, })

def cadastro(request):
    
    projeto_id = request.POST.get('projeto_id')

    if request.POST:
        # Se o parâmetro veio, trata-se de uma alteração.
        if projeto_id:
            #acao = 'alteracao'
            # Recupera um objeto Projeto ou gera o erro 404
            projeto = get_object_or_404(Projeto, pk=projeto_id)

            # Como se trata de uma alteração, o objeto ProjetoForm é instanciado utilizando
            # os dados provenientes do banco de dados (instance=produto) e, em seguida,
            # essas informações são atualizadas utilizando os dados submetidos pelo usuário (request.POST).
            form_projeto = ProjetoForm(request.POST, instance=projeto)
        else:
            #acao = 'inclusao'
            form_projeto = ProjetoForm(request.POST)

        if form_projeto.is_valid():
            # O método save() de ModelForm salva o produto (inclui ou altera) no banco de dados e retorna
            # um objeto do tipo Projeto.
            projeto = form_projeto.save()

            # Se a variável projeto_id for diferente de None então trata-se de uma alteração
            if projeto_id:
                # Gera uma mensagem que será exibida pela página exibe_produto.html através do framework de mensagens.
                messages.add_message(request, messages.INFO, 'Projeto alterado com sucesso.')
            else:
                messages.add_message(request, messages.INFO, 'Projeto cadastrado com sucesso.')

            # Aqui efetuamos um redirect para evitar que um mesmo produto seja cadastrado mais
            # de uma vez caso o usuário aperte a tecla F5 após cadastrar o produto.
            return redirect('appsite:exibe', id=projeto.id)
    else:
        # Ao chegar uma requisição do tipo GET, a página cadastra_produto.html é exibida.
        #acao = 'inclusao'
        form_projeto = ProjetoForm()

    #form_projeto = ProjetoForm()
    context = {'form': form_projeto, }
    return render(request, 'appsite/cadastro.html', context)

def exibe(request, id):
    obj = get_object_or_404(Projeto, pk=id)    
    remove_projeto_form = RemoveProdutoForm(initial={'projeto_id': id})
    projeto = {'projeto': obj, 'linguagem': obj.linguagem.all(), 'remove_projeto_form': remove_projeto_form,}
    return render(request, 'appsite/exibe.html', projeto)

def edita(request):
    projeto = get_object_or_404(Projeto, pk=id)
    formProjeto = ProjetoForm(instance=projeto)
    formProjeto.fields['projeto_id'].initial = projeto.id
    return render(request, 'produto/cadastra_produto.html', {'form': formProjeto, 'acao': 'alteracao'})

def remove(request):
    remove_projeto_form = RemoveProdutoForm(request.POST)
    if remove_projeto_form.is_valid():
        projeto_id = remove_projeto_form.cleaned_data['projeto_id']
        projeto = get_object_or_404(Projeto, pk=projeto_id)
        projeto.delete()
        messages.add_message(request, messages.INFO, 'Projeto removido com sucesso.')
        return render(request, 'appsite/exibe.html', {'projeto': projeto,
                                                              'remove_projeto_form': None})
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar remover um produto')