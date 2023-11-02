#Dentro questo file inserisco tutte le schermate dei FORM che voglio rendere visibile nel FrontEnd
from django import forms #Da fare sempre appena creo il file

#Es creazione del form partendo dal model
from .models import Blog


#Vado a creare la classe per gestire i compi del Form per l'inserimento di un nuovo Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        #fields = '__all__' #Dico di inserire tutti i campi della tabella nel form
        fields = ['titolo','descrizione', 'corpo', 'categoria'] #Dico di inserire solo i campi titolo e descrizione