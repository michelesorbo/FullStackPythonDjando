from django.shortcuts import render
from .models import Carousel
# Create your views here.
def index(request):
    slides = Carousel.objects.filter(pubblicato=True, categoria__nome="Home")
    return render(request, 'account/home.html', {'slides':slides})

def about(request):
    slides = Carousel.objects.filter(pubblicato=True, categoria__nome="About")
    return render(request, 'account/about.html', {'slides':slides})