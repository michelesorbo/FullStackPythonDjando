from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
#Richiamo il decoratore per impedire l'accesso alle pagine se non si è loggati
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfiloEditForm
from .models import Profilo
from django.contrib import messages
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
            #Dopo aver salvato il nuvo utente posso prendere l'id a creare una nuova riga nella tabella profilo con l'id utente appena creato
            Profilo.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html', {'user_form':user_form})


@login_required
def editUser(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profilo_form = ProfiloEditForm(instance=request.user.profilo, data=request.POST,files=request.FILES)

        if user_form.is_valid() and profilo_form.is_valid():
            user_form.save()
            profilo_form.save()
            messages.success(request, 'Profilo aggiornato con successo')
        else:
            messages.error(request, 'Errore profilo non aggiornato')
    else:
        user_form = UserEditForm(instance=request.user)
        profilo_form = ProfiloEditForm(instance=request.user.profilo)
    
    return render(request, 'account/editUser.html', {'user_form':user_form, 'profilo_form':profilo_form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')