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