from django.contrib import admin
from .models import Carousel
# Register your models here.

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'sottotitolo', 'img_preview']
    search_fields = ['titolo', 'sottotitolo', 'corpo']
    list_filter = ['titolo', 'sottotitolo']
    readonly_fields = ['img_preview']