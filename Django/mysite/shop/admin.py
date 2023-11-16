from django.contrib import admin
from .models import Categorie, Prodotti

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria_principale', 'slug']
    prepopulated_fields = {'slug': ('nome', )}

@admin.register(Prodotti)
class ProdottiAdmin(admin.ModelAdmin):
    list_display = ['nome','slug', 'prezzo', 'quantita','pubblicato','categoria','data_modifica']
    search_fields = ['nome', 'descrizione']
    list_filter = ['pubblicato', 'data_inserimento','data_modifica']
    prepopulated_fields = {'slug':('nome',)}
    readonly_fields = ['img_preview']
    list_editable = ['prezzo','quantita','pubblicato']