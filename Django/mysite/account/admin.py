from django.contrib import admin
from .models import Carousel, CarouselCat

# Register your models here.

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'sottotitolo','categoria','img_preview', 'pubblicato']
    search_fields = ['titolo', 'sottotitolo','corpo']
    list_filter = ['categoria','titolo', 'sottotitolo']
    readonly_fields = ['img_preview']

admin.site.register(CarouselCat)