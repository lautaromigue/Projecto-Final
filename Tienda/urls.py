from re import search
from django.urls import path

from Tienda.views import Create_peripheral, Delete_peripheral, Detaile_peripheral, List_peripherals, Update_peripheral, create_game, delete_game, formulario_games, list_games, search_products, update_game, \
    Create_phone, List_phones, Delete_phone, Detaile_phone, Update_phone, \
    List_consoles, Detaile_console, Create_console, Delete_console, Update_console, \
    list_products

urlpatterns = [
    path('create-game/', create_game, name='create_game'),
    path('list-games/', list_games, name='list_games'),
    path('formulario_games/', formulario_games, name = 'formulario'), 
    path('search_products/', search_products, name='search'),
    path('delete-game/<int:pk>/', delete_game, name='delete_game'),
    path('update-game/<int:pk>/', update_game, name='delete_game'),
    
     
    path('create-phone/', Create_phone.as_view(), name= 'Create_phone'),
    path('list-phones/', List_phones.as_view(), name='List_phones'),
    path('detail-phone/<int:pk>/', Detaile_phone.as_view(), name='Detaile_phone'),
    path('delete-phone/<int:pk>/', Delete_phone.as_view(), name='Delete_phone'),
    path('update-phone/<int:pk>/',Update_phone.as_view(), name='Update_phone'),


    path('list-consoles/', List_consoles.as_view(), name='List_peripherals'),  
    path('detail-console/<int:pk>/', Detaile_console.as_view(), name='Detaile_console'), 
    path('create-console/', Create_console.as_view(), name= 'Create_console'), 
    path('delete-console/<int:pk>/', Delete_console.as_view(), name= 'Delete_console'), 
    path('update-console/<int:pk>/', Update_console.as_view(), name='Update_console'),
    
    path('list-peripherals/', List_peripherals.as_view(), name='List_peripherals'),  
    path('detail-peripheral/<int:pk>/', Detaile_peripheral.as_view(), name='Detaile_peripheral'), 
    path('create-peripheral/', Create_peripheral.as_view(), name= 'Create_peripheral'), 
    path('delete-peripheral/<int:pk>/', Delete_peripheral.as_view(), name= 'Delete_peripheral'), 
    path('update-peripheral/<int:pk>/', Update_peripheral.as_view(), name='Update_peripheral'),    
    
    path('list-products/', list_products, name='list_products'),
]