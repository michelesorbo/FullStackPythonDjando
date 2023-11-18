from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart #Vado a prendere i prodotti che sono nella session del carrello
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def order_create(request):
    cart = Cart(request) #Vado a prendere gli elementi che sono nel carrello
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False) #Non posso salvare perchè devo inserire l'utente corrente
            order.user_id = request.user.id #Inserisco l'id dell'utente loggato sul sito
            order.save() #Salvo l'ordine nella tabelle
            #Vado a salvare i prodotti nella tabella Prodotti Ordine
            for item in cart:
                OrderItem.objects.create(order=order,
                                         prodotto=item['prodotto'],
                                         prezzo=item['prezzo'],
                                         quantita=item['quantita'])
            
            #Cancello il carrello
            cart.clear()

            return render(request, 'orders/created.html', {'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form':form})