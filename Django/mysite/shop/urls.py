from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.lista_prodotti, name='lista_prodotti'),
    path('<slug:categoria_slug>', views.lista_prodotti, name='product_list_by_category'), #è la vista dell apagina prodotti filtrata per categoria
    path('<int:id>/<slug:slug>/', views.dettaglio_prodotto, name='dettaglio_prodotto'),#Serve per visualizzare un prodotto nel dettaglio
]
