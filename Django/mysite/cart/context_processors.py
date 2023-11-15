#Mi vado a richiamare tutta l'app
from .cart import Cart

def cart(request):
    return {'cart':Cart(request)}