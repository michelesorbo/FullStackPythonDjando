from django.contrib import admin
from .models import Profilo
# Register your models here.

@admin.register(Profilo)
class ProfiloAdmin(admin.ModelAdmin):
    list_display = ['user', 'data_nascita', 'img']
    raw_id_fields = ['user']