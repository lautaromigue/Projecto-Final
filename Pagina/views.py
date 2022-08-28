from django.shortcuts import render
from django.views.generic import ListView
from Tienda.models import Consoles



class List_consoles(ListView):
    model = Consoles 
    template_name = 'console/list_consoles.html'
