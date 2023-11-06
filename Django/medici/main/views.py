from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.mail import send_mail
#Vado a prendere il modello dalla pagina models
from .models import Blog, Medici, Pazienti

#Regole per la paginazione
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

#Importo la classe dove ho i forms
from .forms import BlogForm, MediciForm, PazientiForm, EmailMedicoForm

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def blog(request):
    blogs_list = Blog.objects.all() #Vado a prendere tutti i blog presenti nella tabella del DB blog
    #Vado a configurare la paginazione
    paginator = Paginator(blogs_list, 3)#Vado a dire quanti blog per pagina devono essere visibili
    page_number = request.GET.get('page',1)

    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request,'blog/index.html', {'blogs':blogs})

def blogSingolo(request,year, month, day, blog, categoria):
    try:
        blog = get_object_or_404(Blog, categoria__slug=categoria, slug=blog, data__year=year, data__month=month, data__day=day) #Mi estrai solo il blog con id = blogs_id
    except Blog.DoesNotExist:
        raise Http404("Blog not find")
    
    return render(request, 'blog/blog.html', {'blog': blog})

#Gestione Pagine Medico Paziente
def medici(request):
    medici_list = Medici.objects.all().order_by('cognome')

    paginator = Paginator(medici_list, 3)#Vado a dire quanti blog per pagina devono essere visibili
    page_number = request.GET.get('page',1)

    try:
        medici = paginator.page(page_number)
    except PageNotAnInteger:
        medici = paginator.page(1)
    except EmptyPage:
        medici = paginator.page(paginator.num_pages)

    return render(request,'main/medici.html', {'medici':medici})

def medico(request, medico_id, medico):
    #medico = Medici.objects.get(pk=medico_id)
    medico = get_object_or_404(Medici, id=medico_id, slug=medico)
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
    pazienti_list = Pazienti.objects.all()
    
    paginator = Paginator(pazienti_list, 3)#Vado a dire quanti blog per pagina devono essere visibili
    page_number = request.GET.get('page',1)

    try:
        pazienti = paginator.page(page_number)
    except PageNotAnInteger:
        pazienti = paginator.page(1)
    except EmptyPage:
        pazienti = paginator.page(paginator.num_pages)
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