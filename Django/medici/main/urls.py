#Gestisco tutte le url dell'application
from django.urls import path

#Importo le view dell'app
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blogs_id>', views.blogSingolo, name='bsingolo')
]