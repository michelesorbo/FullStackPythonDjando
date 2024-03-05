from django.shortcuts import render, redirect
from .models import Carousel
from .forms import ContattiForm
# Create your views here.
def index(request):
    slides = Carousel.objects.filter(pubblicato=True, categoria__nome="Home")
    return render(request, 'account/home.html', {'slides':slides})

def about(request):
    slides = Carousel.objects.filter(pubblicato=True, categoria__nome="About")
    return render(request, 'account/about.html', {'slides':slides})

def contatti(request):
    if request.method == 'POST':
        form = ContattiForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('account:index')
    else:
        form = ContattiForm()
    return render(request, 'account/contatti.html',{'form':form})