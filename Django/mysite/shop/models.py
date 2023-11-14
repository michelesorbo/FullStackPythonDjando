from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
#Per Resize image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
#Per eliminare immagini 
from django_cleanup import cleanup
#Per Editor Avanzato
from ckeditor.fields import RichTextField #Editor senza Upload dei file
# Create your models here.

class Categorie(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome'])
        ]

        verbose_name = 'categorie'
        verbose_name_plural = 'categorie'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])

@cleanup.select 
class Prodotti(models.Model):
    categoria = models.ForeignKey(Categorie, related_name='prodotti', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    img = models.ImageField(upload_to='prodotti/%Y/%m/%d/', default='prodotti/noimg.png')
    img_resize = ImageSpecField(source='img', processors=[ResizeToFill(600,800)], format='PNG', options={'quality':40})
    descrizione = RichTextField(blank=True)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    quantita = models.IntegerField("Quantità in magazzino", default=0)
    pubblicato = models.BooleanField(default=False)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['id','slug']),
            models.Index(fields=['nome']),
            models.Index(fields=['-data_inserimento']),
        ]
        verbose_name = 'prodotti'
        verbose_name_plural = 'prodotti'

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("shop:dettaglio_prodotto", args=[self.id, self.slug])
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')
    