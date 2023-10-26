#In questo file gestisco le path dell view dell'app
from django.urls import path #Richiamo il metodo path di django

from . import views #importo la classe view dell'app

urlpatterns = [
    path('', views.index, name='index'),
    path('michele/', views.michele),
    path('parametro/', views.parametro),
    path('informazioni-sulla-societa/', views.about, name='about'),
    path('contatti/', views.contatti, name='contatti'),
    path('davide/', views.davide, name='davide'),
    path('posts/', views.posts, name='posts'),
]
