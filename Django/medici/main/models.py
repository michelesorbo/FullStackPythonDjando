from django.db import models
from django.utils import timezone

# Create your models here.
class Medici(models.Model):
    #Come codice userò l'id generato dal DB
    nome = models.CharField(max_length=150)
    cognome = models.CharField(max_length=150)
    lugo_nascita = models.CharField(max_length=150)
    data_nascita = models.DateField()
    data_inserimento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cognome} {self.nome}"
    
    class Meta:
        verbose_name_plural = "Medici" #Gestisco il  nome al plurale della tabella


#Vado a gestire le tabelle del BLOG
class categorieBlog(models.Model):
    titolo = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.titolo
    
class Blog(models.Model):
    titolo = models.CharField(max_length=150)
    descrizione = models.CharField(max_length=255)
    corpo = models.TextField()
    categoria = models.ForeignKey(categorieBlog, on_delete=models.CASCADE, default=None)#Vado a prendere la chiave della tabella categoriaBlog e imposti di default nessuna categoria
    data = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.titolo