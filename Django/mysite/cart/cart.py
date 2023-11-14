#Vado a gestire la sessione aggiungendo elementi alla sessione del carrello
from decimal import Decimal
from django.conf import settings
from shop.models import Prodotti

class Cart:
    #Creo il costruttore della classe
    def __init__(self, request):
        """
        Inizializzo il carrello
        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            #Creo e salvo la sessione del carrello vuota, senza oggetti
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
    
    #Aggiorrnare il prezzo in base alla quantità
    def __iter__(self):
        prodotti_ids = self.cart.keys()
        #Prendo i prodotti e li aggiungo al carrello
        prodotti = Prodotti.objects.filter(id__in=prodotti)
        cart = self.cart.copy()
        for prodotto in prodotti:
            cart[str(prodotto.id)]['prodotto'] = prodotto
        for item in cart.values():
            item['prezzo'] = Decimal(item['prezzo'])
            item['prezzo_totale'] = item['prezzo'] * item['quantita']
        
    #Conoscere la quantità di prodotti nel carrello
    def __len__(self):
        return sum(item['quantita'] for item in self.cart.value())

    def add(self, prodotto, quantita=1, override_quantita=False):
        """Aggiungo un prodotto al carrello o aumento la quantità"""

        prodotto_id = str(prodotto.id)

        if prodotto_id not in self.cart:
            self.cart[prodotto_id] = {'quantita':0, 'prezzo': str(prodotto.prezzo)}

        if override_quantita:
            self.cart[prodotto_id]['quantita'] = quantita
        else:
            self.cart[prodotto_id]['quantita'] += quantita
        
        self.save()
    
    #Creo il metodo per salvare le modifiche al carrello
    def save(self):
        self.session.modified = True

    def remove(self, prodotto):
        """Rimuovo un prodotto dal carello"""
        prodotto_id = str(prodotto.id)
        if prodotto_id in self.cart:
            del self.cart[prodotto_id]
            self.save()
        
    #Cacolo il prezzo di tutti i prodotti moltiplicati per le loro quantità
    def fet_total_price(self):
        return sum(Decimal(item['prezzo']) * item['quantita'] for item in self.cart.values())
    
    #Cancellare il carrello dalla sessione
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()