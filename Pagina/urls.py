from django.urls import path
from Pagina.views import List_consoles

urlpatterns = {
    path('list-consoles/', List_consoles.as_view(), name='List_games'),#Al usar una class agregamos el .as_view()
}