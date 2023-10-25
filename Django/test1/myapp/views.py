from django.shortcuts import render
from django.http import HttpResponse #Mi serve per inviare una risposta HTML
# Create your views here.

#Creo il metodo per la pagina HOME del sito. Siccome siamo in ambiente WEB
#Ogni pagina riceve una request
def index(request):
    return HttpResponse("""\
                        <nav>
            <a href='/'>Home</a> - <a href='/michele/'>Michele</a> 
            </nav>Ciao Mondo sono una pagina Python""")

def michele(request):
    return HttpResponse("""\
            <nav>
            <a href='/'>Home</a> - <a href='/michele/'>Michele</a> 
            </nav>
            <h1>Pagina di Michele</h1>
                        <p>Sono un paragrafo</p>

""")