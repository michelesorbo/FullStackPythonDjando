from django.shortcuts import render
from .models import Categorie, Prodotti

# Create your views here.

def lista_prodotti(request):
    categorie = Categorie.objects.all()
    prodotti = Prodotti.objects.all()
    return render(request,'shop/lista_prodotti.html', {'categorie':categorie, 'prodotti':prodotti})