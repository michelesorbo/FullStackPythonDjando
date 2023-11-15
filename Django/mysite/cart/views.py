from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Prodotti
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplicaForm

# Create your views here.

@require_POST
def cart_add(request, prodotto_id):
    cart = Cart(request)
    prodotto = get_object_or_404(Prodotti, id=prodotto_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(prodotto=prodotto, quantita=cd['quantita'], override_quantita=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, prodotto_id):
    cart = Cart(request)
    prodotto = get_object_or_404(Prodotti, id=prodotto_id)
    cart.remove(prodotto)
    return redirect('cart:cart_detail')

#Pagina dettagio carrello
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantita_form'] = CartAddProductForm(initial={
            'quantita':item['quantita'],
            'override':True})
    #Aggiungo il form per il coupon
    coupon_applica_form = CouponApplicaForm()
    return render(request,'cart/detail.html',{'cart':cart, 'coupon_applica_form': coupon_applica_form})
