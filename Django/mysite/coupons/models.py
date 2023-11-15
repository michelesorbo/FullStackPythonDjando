from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Coupon(models.Model):
    codice = models.CharField(max_length=50, unique=True)
    valido_da = models.DateTimeField()
    valido_a = models.DateTimeField()
    sconto = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], 
                                 help_text='Percentuale compresa tra 0 e 100')
    attivo = models.BooleanField()

    def __str__(self):
        return self.codice
