#Gestisco tutte le url dell'application
from django.urls import path

#Importo le view dell'app
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blogs_id>', views.blogSingolo, name='bsingolo'),
    #Inmizio Gestione URL medico paziente
    path('medici/', views.medici, name='medici'),
    path('medico/<int:medico_id>', views.medico, name='medico'),
    path('lista-pazienti/<int:medico_id>', views.pazientiMedico, name='lista_pazienti')
]