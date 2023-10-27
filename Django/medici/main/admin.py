from django.contrib import admin

from .models import Medici, categorieBlog, Blog

# Register your models here.
admin.site.register(Medici)
admin.site.register(categorieBlog)
admin.site.register(Blog)