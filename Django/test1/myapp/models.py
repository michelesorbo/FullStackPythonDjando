from django.db import models
from django.utils import timezone #Serve per gestire le date in django
# Create your models here.

class Post(models.Model):
    titolo = models.CharField(max_length=200) #Creo il campo titolo nel DB di lunghezza 200
    data = models.DateTimeField(default=timezone.now)#Voglio inserire la data in modo automatico
    corpo = models.TextField() #Serve per ricordare testi di grandi dimensioni

    def __str__(self):
        return self.titolo