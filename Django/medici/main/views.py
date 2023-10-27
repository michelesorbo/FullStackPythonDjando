from django.shortcuts import render

#Vado a prendere il modello dalla pagina models
from .models import Blog, Medici, Pazienti

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def blog(request):
    blogs = Blog.objects.all() #Vado a prendere tutti i blog presenti nella tabella del DB blog
    return render(request,'blog/index.html', {'blogs':blogs})

def blogSingolo(request,blogs_id):
    blog = Blog.objects.get(pk=blogs_id) #Mi estrai solo il blog con id = blogs_id
    return render(request, 'blog/blog.html', {'blog': blog})

#Gestione Pagine Medico Paziente
def medici(request):
    medici = Medici.objects.all()
    return render(request,'main/medici.html', {'medici':medici})

def medico(request, medico_id):
    medico = Medici.objects.get(pk=medico_id)
    return render(request, 'main/medico.html', {'medico': medico})

def pazientiMedico(request, medico_id):
    pazienti = Pazienti.objects.all().filter(medico=medico_id) #Seleziono solo i pazienit che hanno id uguale al medico_id passato
    medico = Medici.objects.get(pk=medico_id)
    return render(request,'main/lista_pazienti.html', {'pazienit': pazienti, 'medico':medico})