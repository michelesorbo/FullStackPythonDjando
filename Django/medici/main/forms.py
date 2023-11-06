#Dentro questo file inserisco tutte le schermate dei FORM che voglio rendere visibile nel FrontEnd
from django import forms #Da fare sempre appena creo il file

#Es creazione del form partendo dal model
from .models import Blog, Pazienti, Medici


#Vado a creare la classe per gestire i compi del Form per l'inserimento di un nuovo Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        #fields = '__all__' #Dico di inserire tutti i campi della tabella nel form
        #fields = ['titolo','descrizione', 'corpo', 'categoria'] #Dico di inserire solo i campi titolo e descrizione
        exclude = ['data']

class MediciForm(forms.ModelForm):
    
    class Meta:
        model = Medici
        fields = ("nome","cognome","lugo_nascita","data_nascita","img_medico")

class PazientiForm(forms.ModelForm):
    
    class Meta:
        model = Pazienti
        exclude = ['data_inserimento']

#Creo un Form senza usare un models
class EmailMedicoForm(forms.Form):
    nome = forms.CharField(max_length=100,help_text="Inserisci il tuo nome e cognome")
    email = forms.EmailField(help_text="Inserisi la tua email")
    oggetto = forms.CharField(max_length=150,help_text="Inserisci l'oggetto del messaggio")
    corpo = forms.CharField(required=False, help_text="Inserisi il tuo messaggio", widget=forms.Textarea)


