from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
#Richiamo il decoratore per impedire l'accesso alle pagine se non si è loggati
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
# Create your views here.

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password']) #Richiamo il metodo di Django per verificare l'autenticazione dell'utente

#             if user is not None: #Verifico se l'utente esiste
#                 #Verifico se l'utente è attivo sul sito
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse("Autenticazione avvenuta con successo")
#                 else:
#                     return HttpResponse("Sei stato disattivato dall'amministratore, contattalo per essere riattivato")
#             else:
#                 return HttpResponse('Username o Password Errata')
#     else:#Prima volta che vado sulla pagina di login
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Creo un nuovo oggetto utente ma non lo salvo
            new_user = user_form.save(commit=False)
            #Setto la password
            new_user.set_password(user_form.cleaned_data['password']) #Django codifica la password in SHA256
            #Ora posso salvare in nuovo utente
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html', {'user_form':user_form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')