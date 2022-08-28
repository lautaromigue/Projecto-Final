from re import search
from django.urls import path

from Tienda.views import create_game, delete_game, formulario_games, list_games, \
    create_phone, list_phones, search_products, update_game, \
        List_consoles, Detaile_console, Create_console, Delete_console

urlpatterns = [
    path('create-game/', create_game, name='create_game'),
    path('list-games/', list_games, name='list_games'),
    #path('create-console/', create_console, name= 'create_console'),
    #path('list-consoles/', list_consoles, name='list_consoles'),  
    path('create-phone/', create_phone, name= 'create_phone'),
    path('list-phones/', list_phones, name='list_phones'),
    path('formulario_games/', formulario_games, name = 'formulario'), 
    path('search_products/', search_products, name='search'),
    path('delete-game/<int:pk>/', delete_game, name='delete_game'),
    path('update-game/<int:pk>/', update_game, name='delete_game'),
    path('list-consoles/', List_consoles.as_view(), name='List_games'),  
    path('detail-console/<int:pk>/', Detaile_console.as_view(), name='Detaile_console'), 
    path('create-console/', Create_console.as_view(), name= 'Create_console'), 
    path('delete-console/<int:pk>/', Delete_console.as_view(), name= 'Delete_console'),   
]