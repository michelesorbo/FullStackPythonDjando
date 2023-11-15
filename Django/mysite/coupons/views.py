from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplicaForm
# Create your views here.

@require_POST
def coupon_applica(request):
    now = timezone.now() #Ricoro l'ora e la data di somministrazione del coupon
    form = CouponApplicaForm(request.POST)
    if form.is_valid():
        codice = form.cleaned_data['codice']
        #Vado a vedere se esiste il codice inserito e se il codice è ancora valito o attivo
        try:
            coupon = Coupon.objects.get(codice__iexact=codice, #codice esatto case Sensitive
                                        valido_da__lte=now, #lte (less than or equal to)
                                        valido_a__gte=now, #gte (greater than or equal to)
                                        attivo=True)
            #Siccome stiamo usando il carrello, ti ricordo che il carrello è nella sessione
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
        return redirect('cart:cart_detail')
