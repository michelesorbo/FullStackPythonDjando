from django.shortcuts import render
from django.http import HttpResponse #Mi serve per inviare una risposta HTML
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

def about(request):
    autore = request.GET.get("autore") or ""
    return render(request, 'about.html', {'autore':autore})

def contatti(request):
    return render(request,'contatti.html')

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