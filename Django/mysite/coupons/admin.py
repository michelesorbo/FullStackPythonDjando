from django.contrib import admin
from .models import Coupon
# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['codice','valido_da','valido_a','sconto','attivo']
    list_filter = ['attivo', 'valido_da','valido_a']
    search_fields = ['codice']