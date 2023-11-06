from django.db import models
from django.utils import timezone
from django.urls import reverse #Serve per riscrivere un url

#Vado a prendere il modello standard di Django per la gestione degli utenti
from django.contrib.auth.models import User

#Per immagine preview in admin
from django.utils.html import mark_safe

# Create your models here.
class Medici(models.Model):
    #Come codice userò l'id generato dal DB
    slug = models.SlugField(max_length=200, default="")
    nome = models.CharField(max_length=150)
    cognome = models.CharField(max_length=150)
    lugo_nascita = models.CharField('Luogo di Nascita',max_length=150)
    data_nascita = models.DateField('Data di Nascita')
    email = models.EmailField(blank=True, null=True, default="")
    img_medico = models.ImageField("Immagine del profilo", null=True, blank=True, upload_to="mediciimg/", default="mediciimg/no_img.png")
    data_inserimento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cognome} {self.nome}"
    
    def get_absolute_url(self):
        return reverse("medico", args=[self.id, self.slug])
    
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.img_medico.url}" width="150" />')
    
    class Meta:
        verbose_name_plural = "Medici" #Gestisco il  nome al plurale della tabella

#Vado a creare la tabella paziente
class Pazienti(models.Model):
    slug = models.SlugField(max_length=200, default="")
    nome = models.CharField(max_length=150)
    cognome = models.CharField(max_length=150)
    luogo_nascita = models.CharField('Luogo di Nascita',max_length=150)
    data_nascita = models.DateField('Data di Nascita')
    residenza = models.CharField('Comune di Residenza', max_length=150)
    indirizzo = models.CharField(max_length=200)
    medico = models.ForeignKey(Medici, on_delete=models.CASCADE, default=None)
    data_inserimento = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.cognome} {self.nome}"
    
    class Meta:
        verbose_name_plural = "Pazienti"


#Vado a gestire le tabelle del BLOG
class categorieBlog(models.Model):
    titolo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default="")
    descrizione = models.CharField(max_length=150, default="")

    def __str__(self) -> str:
        return f"{self.titolo}"
    
class Blog(models.Model):
    titolo = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique_for_date='data')
    descrizione = models.CharField(max_length=255)
    corpo = models.TextField()
    categoria = models.ForeignKey(categorieBlog, on_delete=models.CASCADE, default=None)#Vado a prendere la chiave della tabella categoriaBlog e imposti di default nessuna categoria
    img_blog = models.ImageField("Immagine di copertina", null=True, blank=True, upload_to="blogimg/", default="blogimg/no_img.jpeg")
    data = models.DateTimeField(default=timezone.now)
    #Vado ad aggiungere l'utente che ha creato il blog
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')

    def __str__(self) -> str:
        return self.titolo
    
    #Riscrivo la url
    def get_absolute_url(self):
        return reverse("bsingolo", args=[self.categoria.slug, self.data.year, self.data.month, self.data.day, self.slug])
    

    #Per visualizzare immagine in Admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.img_blog.url}" width="150" />')