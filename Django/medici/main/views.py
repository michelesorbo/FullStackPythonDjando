from django.shortcuts import render
from django.http import Http404
#Vado a prendere il modello dalla pagina models
from .models import Blog, Medici, Pazienti

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
    return render(request, 'main/medico.html', {'medico': medico})

def pazientiMedico(request, medico_id):
    pazienti = Pazienti.objects.filter(medico=medico_id).order_by('cognome') #Seleziono solo i pazienit che hanno id uguale al medico_id passato
    medico = Medici.objects.get(pk=medico_id)
    return render(request,'main/lista_pazienti.html', {'pazienit': pazienti, 'medico':medico})