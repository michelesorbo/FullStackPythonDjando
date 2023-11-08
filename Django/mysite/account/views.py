from django.shortcuts import render
from .models import Carousel
# Create your views here.
def index(request):
    slides = Carousel.objects.all()
    return render(request, 'account/home.html', {'slides':slides})