from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
#Richiamo il decoratore per impedire l'accesso alle pagine se non si è loggati
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password']) #Richiamo il metodo di Django per verificare l'autenticazione dell'utente

            if user is not None: #Verifico se l'utente esiste
                #Verifico se l'utente è attivo sul sito
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Autenticazione avvenuta con successo")
                else:
                    return HttpResponse("Sei stato disattivato dall'amministratore, contattalo per essere riattivato")
            else:
                return HttpResponse('Username o Password Errata')
    else:#Prima volta che vado sulla pagina di login
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')