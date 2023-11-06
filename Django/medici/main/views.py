from django.shortcuts import render, redirect
from django.http import Http404
from django.core.mail import send_mail
#Vado a prendere il modello dalla pagina models
from .models import Blog, Medici, Pazienti

from django.contrib.auth.decorators import login_required

#Importo la classe dove ho i forms
from .forms import BlogForm, MediciForm, PazientiForm, EmailMedicoForm

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def blog(request):
    blogs = Blog.objects.all() #Vado a prendere tutti i blog presenti nella tabella del DB blog
    return render(request,'blog/index.html', {'blogs':blogs})

def blogSingolo(request,blogs_id):
    try:
        blog = Blog.objects.get(pk=blogs_id) #Mi estrai solo il blog con id = blogs_id
    except Blog.DoesNotExist:
        raise Http404("Blog not find")
    
    return render(request, 'blog/blog.html', {'blog': blog})

#Gestione Pagine Medico Paziente
def medici(request):
    medici = Medici.objects.all().order_by('cognome')
    return render(request,'main/medici.html', {'medici':medici})

def medico(request, medico_id):
    medico = Medici.objects.get(pk=medico_id)
    send = False

    form = EmailMedicoForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data #Prendo i dati puliti che hanno passato la validazione
        subject = f"{cd['nome']} ti raccomanda di leggere il messaggio con titolo: {cd['oggetto']}"
        message = cd['corpo']
        sender = cd['email']
        send_mail(subject, message,sender,['reciver@exemple.com'])
        send = True
        form = EmailMedicoForm() #Serve per resettare i campi del form
    else:
        form = EmailMedicoForm()

    return render(request, 'main/medico.html', {'medico': medico, 'form':form, 'send':send})

def pazientiMedico(request, medico_id):
    pazienti = Pazienti.objects.filter(medico=medico_id).order_by('cognome') #Seleziono solo i pazienit che hanno id uguale al medico_id passato
    medico = Medici.objects.get(pk=medico_id)
    return render(request,'main/lista_pazienti.html', {'pazienti': pazienti, 'medico':medico})

def pazienti(request):
    pazienti = Pazienti.objects.all()
    return render(request, 'main/pazienti.html', {'pazienti':pazienti})

#Creo la view per creare un nuovo blog nel Front End
@login_required
def newBlog(request):
    if request.method == 'POST': #Se ricevo una richiesta di tipo POST (significa che ho compilato e inviato il form)
        form = BlogForm(request.POST, files=request.FILES) #Salva tutti i campi del form inizializzati con i valori messi nelle input del form
        if form.is_valid(): #Verifico se i dati sono validi
            blog = form.save() #Salvo i dati nel DB e ricordo nella variabile blog l'id appena asseganto al blog
            return redirect('bsingolo', blog.id) #Richiamo la pagina 'bsingolo' (è il nome che diamo al path nel file urls) e gli passo l'id del blog appena creato
    else: #Se non arriva la richiesta POST creo il form vuoto
        form = BlogForm()
    return render(request, 'blog/newblog.html', {'form': form})

@login_required
def newMedico(request):
    if request.method == 'POST': #Se ricevo una richiesta di tipo POST (significa che ho compilato e inviato il form)
        form = MediciForm(request.POST, files=request.FILES) #Salva tutti i campi del form inizializzati con i valori messi nelle input del form
        if form.is_valid(): #Verifico se i dati sono validi
            medico = form.save() #Salvo i dati nel DB e ricordo nella variabile blog l'id appena asseganto al blog
            return redirect('medico', medico.id) #Richiamo la pagina 'bsingolo' (è il nome che diamo al path nel file urls) e gli passo l'id del blog appena creato
    else: #Se non arriva la richiesta POST creo il form vuoto
        form = MediciForm()
    return render(request, 'main/newMedico.html', {'form': form})

@login_required
def newPaziente(request):
    if request.method == 'POST': #Se ricevo una richiesta di tipo POST (significa che ho compilato e inviato il form)
        form = PazientiForm(request.POST) #Salva tutti i campi del form inizializzati con i valori messi nelle input del form
        if form.is_valid(): #Verifico se i dati sono validi
            paziente = form.save() #Salvo i dati nel DB e ricordo nella variabile blog l'id appena asseganto al blog
            return redirect('medici') #Richiamo la pagina 'bsingolo' (è il nome che diamo al path nel file urls) e gli passo l'id del blog appena creato
    else: #Se non arriva la richiesta POST creo il form vuoto
        form = PazientiForm()
    return render(request, 'main/newPaziente.html', {'form': form})

def EmailMedico(request, medico_id):
    medico = Medici.objects.get(pk=medico_id)
    send = False
    form = EmailMedicoForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data #Prendo i dati puliti che hanno passato la validazione
        subject = f"{cd['nome']} ti raccomanda di leggere il messaggio con titolo: {cd['oggetto']}"
        message = cd['corpo']
        sender = cd['email']
        send_mail(subject, message,sender,['reciver@exemple.com'])
        send = True
        form = EmailMedicoForm() #Serve per resettare i campi del form
    else:
        form = EmailMedicoForm()
    return render(request, 'main/emailMedico.html', {'form':form, 'medico':medico, 'send':send})