#Gestisco tutte le url dell'application
from django.urls import path

#Importo le view dell'app
from . import views

#app_name = 'blog'

urlpatterns = [
    path('',views.index, name='index'),
    path('lista-articoli/', views.blog, name='blog'),
    path('blog/<slug:categoria>/<int:year>/<int:month>/<int:day>/<slug:blog>/', views.blogSingolo, name='bsingolo'),
    path('nuovo-blog/', views.newBlog, name='newBlog'),
    #Inmizio Gestione URL medico paziente
    path('medici/', views.medici, name='medici'),
    path('medico/<int:medico_id>/<slug:medico>', views.medico, name='medico'),
    path('emailMedico/<int:medico_id>', views.EmailMedico, name='emailMmedico'),
    path('nuovo-medico/', views.newMedico, name='newMedico'),
    path('nuovo-paziente/', views.newPaziente, name='newPaziente'),
    path('pazienti/', views.pazienti, name='pazienti'),
    path('lista-pazienti/<int:medico_id>', views.pazientiMedico, name='lista_pazienti')
]