from django.db import models
#Per immagine preview in admin
from django.utils.html import mark_safe
# Create your models here.
class Carousel(models.Model):
    titolo = models.CharField("Titolo della slide", max_length=200)
    sottotitolo = models.CharField("Sottotitolo della slide", max_length=250, blank=True, null=True)
    corpo = models.TextField("Contenuto della slide")
    img = models.ImageField("Immagine Slide", upload_to='slide/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.titolo
    
    #Per visualizzare immagine in Admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')