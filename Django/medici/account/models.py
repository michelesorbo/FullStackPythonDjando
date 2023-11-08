from django.db import models
from django.conf import settings

# Create your models here.

class Profilo(models.Model):
    #link: https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#django.contrib.auth.get_user_model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_nascita = models.DateField("data di nascita",blank=True, null=True)
    img = models.ImageField("Immagine di profilo", upload_to='user/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profito di {self.user.username}'
