from django.db import models
#Per immagine preview in admin
from django.utils.html import mark_safe

#Librerie per Resize Img
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToCover

#Per cancellare le immagini
from django_cleanup import cleanup

#Per caricare l'editor di testo avanzato
from ckeditor.fields import RichTextField #Senza la funzione di upload delle immagini
from ckeditor_uploader.fields import RichTextUploadingField #Con la possibilità di fare l'upload delle immagini

# Create your models here.
#Modelli per Slide
class CarouselCat(models.Model):
    nome = models.CharField("Nome della categoria", max_length=150)

    def __str__(self):
        return self.nome
    
@cleanup.select
class Carousel(models.Model):
    titolo = models.CharField("Titolo della slide", max_length=200)
    sottotitolo = models.CharField("Sottotitolo della slide", max_length=250, blank=True, null=True)
    #corpo = models.TextField("Contenuto della slide")
    corpo = RichTextUploadingField("Contenuto delle slide")
    categoria = models.ForeignKey(CarouselCat, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField("Immagine Slide", upload_to='slide/%Y/%m/', default='slide/no_img.jpeg')
    img_resize = ImageSpecField(source='img', processors=[ResizeToCover(800, 800)], format='PNG', options={'quality': 60})
    pubblicato = models.BooleanField("Pubblicato", default=False)

    def __str__(self):
        return self.titolo
    
    #Per visualizzare immagine in Admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')