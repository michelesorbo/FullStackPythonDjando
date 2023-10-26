from django.db import models
from django.utils import timezone #Serve per gestire le date in django
# Create your models here.

class Post(models.Model):
    titolo = models.CharField(max_length=200) #Creo il campo titolo nel DB di lunghezza 200
    data = models.DateTimeField(default=timezone.now)#Voglio inserire la data in modo automatico
    corpo = models.TextField() #Serve per ricordare testi di grandi dimensioni

    def __str__(self):
        return f"Scrivo quello che voglio: {self.titolo}"
    
class Articolo(models.Model):
    titolo = models.CharField(max_length=150)
    descrizione = models.CharField(max_length=255)
    corpo = models.TextField()
    data_creazione = models.DateTimeField(default=timezone.now)
    data_ultima_modifica = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name_plural = 'Articoli'#Per dare il nome giusto al plurale