from django.db import models
from shop.models import Prodotti
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    indirizzo = models.CharField(max_length=250)
    cap = models.CharField('C.A.P.',max_length=20, validators=[RegexValidator(
        regex=r'^[0-9]{5}$',
        message='Inserisci un C.A.P. valido',
    )])
    citta = models.CharField(max_length=100)
    creato = models.DateTimeField(auto_now_add=True)
    modificato = models.DateTimeField(auto_now=True)
    pagato = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creato']
        indexes = [
            models.Index(fields=['-creato']),
        ]

    def __str__(self):
        return f'Ordine {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotti,related_name='order_items',on_delete=models.CASCADE)
    prezzo = models.DecimalField(max_digits=10,decimal_places=2)
    quantita = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.prezzo * self.quantita
