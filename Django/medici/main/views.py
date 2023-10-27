from django.shortcuts import render

#Vado a prendere il modello dalla pagina models
from .models import Blog

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def blog(request):
    blogs = Blog.objects.all() #Vado a prendere tutti i blog presenti nella tabella del DB blog
    return render(request,'blog/index.html', {'blogs':blogs})

def blogSingolo(request,blogs_id):
    blog = Blog.objects.get(pk=blogs_id) #Mi estrai solo il blog con id = blogs_id
    return render(request, 'blog/blog.html', {'blog': blog})