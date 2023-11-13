from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.lista_prodotti, name='lista_prodotti'),
]
