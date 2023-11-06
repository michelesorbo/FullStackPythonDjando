from django.contrib import admin

from .models import Medici, categorieBlog, Blog, Pazienti

# Register your models here.
class MediciAdmin(admin.ModelAdmin):
    list_display = ['cognome','nome','lugo_nascita','data_nascita', 'img_preview']
    search_fields = ['cognome', 'nome', 'data_nascita']
    list_filter = ['data_inserimento', 'lugo_nascita']
    readonly_fields = ['img_preview']
    prepopulated_fields = {'slug':('nome','cognome',)}
admin.site.register(Medici, MediciAdmin)

#Registro i Pazienit
@admin.register(Pazienti)
class PazientiAdmin(admin.ModelAdmin):
    list_display = ['cognome','nome','residenza','medico']
    search_fields = ['cognome', 'nome', 'data_nascita', 'residenza', 'luogo_nascita']
    list_filter = ['residenza', 'luogo_nascita']

class catBlog(admin.ModelAdmin):
    list_display = ['titolo','descrizione']
    search_fields = ['titolo','descrizione']
    prepopulated_fields = {'slug':('titolo',)} #Serve a popolare un campo in base ad un'altro campo del form
admin.site.register(categorieBlog, catBlog)

#Prima di registrare il modulo blog in admin, gli applico delle personalizzazioni alla visualizzazione della tabelle
#Lo faccio creando una classe
#@admin.register(Blog) #Alternativa con Decoratore
class BlogAdmin(admin.ModelAdmin):
    list_display = ['titolo','slug','descrizione','categoria','autore','data', 'img_preview'] #Crea le colonne nella visualizzazione del blog
    search_fields = ['titolo','descrizione'] #Creo una barra di ricerca e specifico su quali campi della tabella deve cercare
    list_filter = ['categoria','autore','data'] #Menù laterale con il filtro dei campi desiderati
    readonly_fields = ['img_preview'] #Per visualizzare immagine in Admin
    prepopulated_fields = {'slug':('titolo',)} #Serve a popolare un campo in base ad un'altro campo del form
#Dopo aver creato la classe la applico al modulo
admin.site.register(Blog, BlogAdmin)