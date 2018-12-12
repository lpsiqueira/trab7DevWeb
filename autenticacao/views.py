from django.shortcuts import render, redirect
from .forms import Login
from django.contrib.auth import authenticate, login

# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = Login(request.POST)

        if form.is_valid():
            usernm = form.cleaned_data['username']
            psswrd = form.cleaned_data['password']
            user = authenticate(username=usernm, password=psswrd)

            if user is not None:
                saida = True
                return redirect('appsite:busca')
            
            else:
                saida = False
                return redirect('appsite:cadastro')
            
            #return redirect('autenticacao:autenticado', val=saida)
            #return autenticado(request, saida)
    else:
        form = Login()

    return render(request, 'autenticacao/signin.html', {'form': form})