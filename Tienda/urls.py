from re import search
from django.urls import path

from Tienda.views import create_game, delete_game, formulario_games, list_games, update_game, Detail_game, \
    create_phone, delete_phone, list_phones, formulario_phones, update_phone, Detaile_phone, \
    list_consoles, delete_console, create_console, formulario_consoles, update_console, Detail_console,  \
    create_peripheral, delete_peripheral, Detaile_peripheral, formulario_peripherals, list_peripherals, update_peripheral, formulario_peripherals, \
    list_products, search_product

urlpatterns = [
    path('create-game/', create_game, name='create_game'),
    path('list-games/', list_games, name='list_games'),
    path('formulario_games/', formulario_games, name = 'formulario'), 
    path('delete-game/<int:pk>/', delete_game, name='delete_game'),
    path('update-game/<int:pk>/', update_game, name='update_game'),
    path('detail-game/<int:pk>/', Detail_game.as_view(), name='Detail_game'),
 

    path('create-console/', create_console, name='create_console'),
    path('list-consoles/', list_consoles, name='list_consoles'),
    path('formulario_consoles/', formulario_consoles, name = 'formulario_console'), 
    path('delete-console/<int:pk>/', delete_console, name='delete_console'),
    path('update-console/<int:pk>/', update_console, name='update_console'),
    path('detail-console/<int:pk>/', Detail_console.as_view(), name='Detaile_console'),
    


    path('create-phone/', create_phone, name='create_phone'),
    path('list-phones/', list_phones, name='list_phones'),
    path('formulario_phones/', formulario_phones, name = 'formulario_phone'), 
    path('delete-phone/<int:pk>/', delete_phone, name='delete_phone'),
    path('update-phone/<int:pk>/', update_phone, name='update_phone'),
    path('detail-phone/<int:pk>/', Detaile_phone.as_view(), name='Detaile_phone'),
    
       
    
    path('create-peripheral/', create_peripheral, name='create_peripheral'),
    path('list-peripherals/', list_peripherals, name='list_peripherals'),
    path('formulario_peripherals/', formulario_peripherals, name = 'formulario_peripheral'), 
    path('delete-peripheral/<int:pk>/', delete_peripheral, name='delete_peripheral'),
    path('update-peripheral/<int:pk>/', update_peripheral, name='update_peripheral'),
    path('detail-peripheral/<int:pk>/', Detaile_peripheral.as_view(), name='Detaile_peripheral'),
    
    path('list-products/', list_products, name='list_products'),
    path('search-product/', search_product, name='search_product')
]