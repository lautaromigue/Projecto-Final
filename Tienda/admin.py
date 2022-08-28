from django.contrib import admin
from Tienda.models import Consoles, Games, Peripherals, Phones

# Register your models here.

@admin.register(Games)
class Games_admin(admin.ModelAdmin):
    list_display = ['name','price','stock','game_company','image']

@admin.register(Consoles)
class Consoles_admion(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'producer', 'image']
    
@admin.register(Phones)
class Phones_admion(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'producer', 'image']

@admin.register(Peripherals)
class Peripherals_admion(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'producer', 'image']
