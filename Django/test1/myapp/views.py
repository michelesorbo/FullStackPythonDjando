from django.shortcuts import render
from django.http import HttpResponse #Mi serve per inviare una risposta HTML
# Create your views here.

#Creo il metodo per la pagina HOME del sito. Siccome siamo in ambiente WEB
#Ogni pagina riceve una request
def index(request):
    return HttpResponse("Ciao Mondo sono una pagina Python")