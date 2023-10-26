from django.shortcuts import render
from django.http import HttpResponse #Mi serve per inviare una risposta HTML

#Importo i models da visualizzare nel frontend
from .models import Post, Articolo
# Create your views here.

#Creo il metodo per la pagina HOME del sito. Siccome siamo in ambiente WEB
#Ogni pagina riceve una request
def index(request):
    # return HttpResponse("""\
    #                     <nav>
    #         <a href='/'>Home</a> - <a href='/michele/'>Michele</a> 
    #         </nav>Ciao Mondo sono una pagina Python
    #                     """)
    msg = "Ciao sono il messagigo di view"
    autore = "Carlo"
    articoli = [
        "Sono il primo articolo",
        "Sono il secondo articolo",
        "Sono il terzo articolo"
        ]
    
    dati = {
        'titolo':"Titolo 1",
        'data': "27/10/2012",
        'corpo': "Sono il contenuto del dato"
    }
    return render(request,'index.html', {'messaggio': msg, 'autore': autore, 'articoli':articoli, 'dati':dati})

#Pagine Post
def posts(require):
    posts = Post.objects.all() #Serve per estrarre tutti i dati della tabella post nel db e salvarla nella variabile posts
    return render(require,'posts.html', {'posts': posts})

def articoli(request):
    articoli = Articolo.objects.all()
    return render(request,'articoli.html', {'articoli':articoli})

def about(request):
    autore = request.GET.get("autore") or ""
    return render(request, 'about.html', {'autore':autore})

def contatti(request):
    return render(request,'contatti.html')

def davide(request):

    titolo = request.GET.get('titolo') or 'nessun titolo'

    articolo4 = {
        'data': '15/12/2023',
        'titolo': 'Corso Python Avanzato',
        'corpo': 'Benvenuti alla prima lezione del corso di Python avanzato'
    }

    articolo3 = {
        'data': '15/12/2022',
        'titolo': 'Corso C++',
        'corpo': 'Benvenuti alla prima lezione del corso di C++'
    }

    articolo2 = {
        'data': '22/12/2022',
        'titolo': 'Corso JAVA',
        'corpo': 'Benvenuti alla prima lezione del corso di JAVA'
    }

    articolo1 = {
        'data': '22/11/2022',
        'titolo': 'Corso Python',
        'corpo': 'Benvenuti alla prima lezione del corso di Python'
    }

    articoli = [articolo1,articolo2,articolo3, articolo4]
    return render(request,'davide.html', {'autore': 'Davide', 'articoli': articoli, 'ricerca':titolo})

def michele(request):
    return HttpResponse("""\
            <nav>
            <a href='/'>Home</a> - <a href='/michele/'>Michele</a> 
            </nav>
            <h1>Pagina di Michele</h1>
                        <p>Sono un paragrafo</p>

""")

#Come prendere parametri dalla url localhost:8000/?nome=Carlo
def parametro(request):
    nome = request.GET.get("nome") or "Nessun Nome"
    cognome = request.GET.get("cognome") or "Nessun Cognome"
    return HttpResponse(f"Ciao, {format(nome)} {format(cognome)}")