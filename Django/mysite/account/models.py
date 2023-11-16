from django.db import models
#Per immagine preview in admin
from django.utils.html import mark_safe

#Librerie per Resize Img
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToCover

#Per cancellare le immagini
from django_cleanup import cleanup

#Per caricare l'editor di testo avanzato
from ckeditor.fields import RichTextField #Senza la funzione di upload delle immagini
from ckeditor_uploader.fields import RichTextUploadingField #Con la possibilità di fare l'upload delle immagini

#Librerie per Espandere le informazioni su utenti
from django.contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

#Vado ad importare il validatore tramite regex
from django.core.validators import RegexValidator

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
    

#MODELS PER UTENTI
#Vado ad incrementare le informazioni di base sull'utente
@cleanup.select
class UserProfile(models.Model): 

    #Creo le scelte per il campo di tipo select
    ACCOUNT_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('developer', 'Developer'),
        ('cliente', 'Cliente')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE) #Creo la relazione uno a uno con Utente
    data_nascita = models.DateField("Data di nascita", null=True, blank=True)
    cf = models.CharField("Codice Fiscale", max_length=16, blank=True, null=True, validators=[RegexValidator(
        regex=r'^[A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9]{3}[A-Za-z]{1}$', #r'(?i...)' metodo Carlo
        message='Inserisci un Codice Fiscale valido',
    )])
    tipo_account = models.CharField("Tipologi Utente", max_length=50, default='cliente', choices=ACCOUNT_TYPE_CHOICES)
    img_profilo = ProcessedImageField(upload_to='user_profile/%Y/%m/%d/', processors=[ResizeToCover(128,128)], format='PNG', options={'quality':60}, default='user_profile/profile_user.png')
    indirizzo = models.CharField(max_length=250, blank=True, null=True)
    comune = models.CharField(max_length=150, blank=True, null=True)
    citta = models.CharField("Città", max_length=150, blank=True, null=True)
    cap = models.CharField("C.A.P.", max_length=5, blank=True, null=True, validators=[RegexValidator(
        regex=r'^[0-9]{5}$',#Scrivo l'espressione Regolare
        message='Inseriesci un CAP valido',#Errore da far comparire sul campo in caso di errore
    )])

    def __str__(self):
        return self.user.username
    
    #Metodo per visulizzare l'immagine in admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.img_profilo.url}" width="100" />')
    

    #Salvo il CF in Maiuscolo nel DB
    def save(self, *args, **kwargs):
        if self.cf:
            self.cf = self.cf.upper()
            super(UserProfile, self).save(*args, **kwargs)
        return None
    
    #Salvo il profilo utente appena si crea un nuovo utente nel DB
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)