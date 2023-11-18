from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
#Vado a mettere nel degglio ordine i prodoti come tabella
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['prodotto']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'indirizzo', 'citta','cap', 'creato','modificato', 'pagato']
    list_filter = ['pagato', 'creato','modificato']
    raw_id_fields = ['user']
    inlines = [OrderItemInline]