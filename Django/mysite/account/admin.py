from django.contrib import admin
from .models import Carousel, CarouselCat, UserProfile
#Per aggiungere UserProfile dentro la vista User
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'sottotitolo','categoria','img_preview', 'pubblicato']
    search_fields = ['titolo', 'sottotitolo','corpo']
    list_filter = ['categoria','titolo', 'sottotitolo']
    readonly_fields = ['img_preview']
    list_editable = ['pubblicato']

admin.site.register(CarouselCat)

#Area Utenti
class CustomUserAdmin(admin.StackedInline): #Serve a inserire nella visualizzazione User altre tabelle
    model= UserProfile
    can_delete = False
    readonly_fields = ['img_preview']

#Creo la nuva visualizzazione dell'account User in Admin
class AccountsUserAdmin(UserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccountsUserAdmin, self).add_view(*args,**kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [CustomUserAdmin]
        return super(AccountsUserAdmin, self).change_view(*args,**kwargs)

admin.site.unregister(User)
admin.site.register(User,AccountsUserAdmin)