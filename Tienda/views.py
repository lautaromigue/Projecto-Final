from http.client import HTTPResponse
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from re import search
from Tienda.models import Games, Consoles, Phones, Peripherals
from Tienda.forms import formulario_for_consoles, formulario_for_games
from django.views.generic import ListView, DetailView, CreateView, DeleteView   
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# GAMES

@login_required
def create_game(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = formulario_for_games(request.POST, request.FILES)
            
            if form.is_valid():
                Games.objects.create(
                    name = form.cleaned_data['name'],
                    price = form.cleaned_data['price'],
                    stock = form.cleaned_data['stock'],
                    game_company = form.cleaned_data['game_company'],
                    image = form.cleaned_data['image'],
                )

                return redirect(list_products)
            
        elif request.method == 'GET':
            form = formulario_for_games()
            context = {'form':form}
            return render(request, 'games/create_game.html', context=context)
    return redirect ("login")    

@login_required
def list_games(request):
    games = Games.objects.all()
    context = {
        'games':games
    }
    return render(request, 'games/list_games.html', context = context)

@login_required
def formulario_games(request):
    print(request.method)
    if request.method == 'POST': 
        print(request.POST)
    return render(request, 'games/formulario_games.html', context={})

@login_required
def delete_game(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
                game = Games.objects.get(pk=pk)
                context = {'game':game}
                return render(request, 'games/delete_game.html', context=context)
        
        elif request.method == 'POST':
                game = Games.objects.get(pk=pk)
                game.delete()
                return redirect(list_products)
    return redirect ("login")        

@login_required
def update_game(request, pk):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = formulario_for_games(request.POST)
            if form.is_valid():
                game = Games.objects.get(id=pk)
                game.name = form.cleaned_data['name']
                game.price = form.cleaned_data['price']
                game.stock = form.cleaned_data['stock']
                game.game_company = form.cleaned_data['game_company']
                game.save()
            return redirect(list_products)
        
        elif request.method == 'GET':
            game = Games.objects.get(id=pk)
            form = formulario_for_games(initial={
                                            'name':game.name, 
                                            'price':game.price, 
                                            'stock':game.stock, 
                                            'game_company':game.game_company})
            context = {'form':form}
            return render(request, 'games/update_game.html', context=context)
    return redirect ("login")           


class Detail_game(DetailView):
    model = Games
    template_name = 'games/detail_game.html'


#CONSOLES

# class List_consoles(LoginRequiredMixin,ListView):
#     model = Consoles
#     template_name = 'consoles/list_consoles.html'
    
class Detail_console(DetailView):
    model = Consoles
    template_name = 'consoles/detail_console.html'
    
# class Create_console(CreateView):
#     model = Consoles
#     template_name = 'consoles/create_console.html'
#     fields = '__all__'
#     success_url = '/Tienda/list-consoles/'

# class Delete_console(DeleteView):
#     model = Consoles
#     template_name = 'consoles/delete_console.html'
#     success_url = '/Tienda/list-consoles/'        

# class Update_console(UpdateView):
#     model = Consoles
#     template_name = 'consoles/update_console.html'
#     fields = '__all__'
#     success_url = '/Tienda/list-consoles/' 


@login_required
def create_console(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = formulario_for_consoles(request.POST, request.FILES)
            
            if form.is_valid():
                Consoles.objects.create(
                    name = form.cleaned_data['name'],
                    price = form.cleaned_data['price'],
                    stock = form.cleaned_data['stock'],
                    producer = form.cleaned_data['producer'],
                    image = form.cleaned_data['image'],
                )

                return redirect(list_products)
            
        elif request.method == 'GET':
            form = formulario_for_consoles()
            context = {'form':form}
            return render(request, 'consoles/create_console.html', context=context)
    return redirect ("login")    
 


@login_required
def list_consoles(request):
    consoles = Consoles.objects.all()
    context = {
        'consoles':consoles
    }
    return render(request, 'consoles/list_consoles.html', context = context)



@login_required
def formulario_consoles(request):
    print(request.method)
    if request.method == 'POST': 
        print(request.POST)
    return render(request, 'consoles/formulario_consoles.html', context={})



@login_required
def delete_console(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
                console = Consoles.objects.get(pk=pk)
                context = {'console':console}
                return render(request, 'consoles/delete_console.html', context=context)
        
        elif request.method == 'POST':
                console = Consoles.objects.get(pk=pk)
                console.delete()
                return redirect(list_products)
    return redirect ("login")        



@login_required
def update_console(request, pk):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = formulario_for_consoles(request.POST)
            if form.is_valid():
                console = Consoles.objects.get(id=pk)
                console.name = form.cleaned_data['name']
                console.price = form.cleaned_data['price']
                console.stock = form.cleaned_data['stock']
                console.producer = form.cleaned_data['producer']
                console.save()
                
                return redirect(list_products)
        
        elif request.method == 'GET':
            console = Consoles.objects.get(id=pk)
            form = formulario_for_consoles(initial={
                                            'name':console.name, 
                                            'price':console.price, 
                                            'stock':console.stock, 
                                            'producer':console.producer})
            context = {'form':form}
            return render(request, 'consoles/update_console.html', context=context)
    return redirect ("login")  






#PHONES


class List_phones(LoginRequiredMixin,ListView):
    model = Phones 
    template_name = 'phones/list_phones.html'
    

class Detaile_phone(LoginRequiredMixin,DetailView):
    model = Phones
    template_name = 'phones/detail_phone.html'
    
class Create_phone(LoginRequiredMixin,CreateView):
    model = Phones
    template_name = 'phones/create_phone.html'
    fields = '__all__'
    success_url = '/Tienda/list-phones/'

class Delete_phone(LoginRequiredMixin,DeleteView):
    model = Phones
    template_name = 'phones/delete_phone.html'
    success_url = '/Tienda/list-phones/'        

class Update_phone(LoginRequiredMixin,UpdateView):
    model = Phones
    template_name = 'phones/update_phone.html'
    fields = '__all__'
    success_url = '/Tienda/list-phones/' 




# PERIPHERALS


class List_peripherals(LoginRequiredMixin,ListView):
    model = Peripherals
    template_name = 'peripherals/list_peripherals.html'
    
class Detaile_peripheral(LoginRequiredMixin,DetailView):
    model = Peripherals
    template_name = 'peripherals/detail_peripheral.html'
    
class Create_peripheral(LoginRequiredMixin,CreateView):
    model = Peripherals
    template_name = 'peripherals/create_peripheral.html'
    fields = '__all__'
    success_url = '/Tienda/list-peripherals/'

class Delete_peripheral(LoginRequiredMixin,DeleteView):
    model = Peripherals
    template_name = 'peripherals/delete_peripheral.html'
    success_url = '/Tienda/list-peripherals/'        

class Update_peripheral(LoginRequiredMixin,UpdateView):
    model = Peripherals
    template_name = 'peripherals/delete_peripheral.html'
    fields = '__all__'
    success_url = '/Tienda/list-peripherals/'



@login_required
def list_products(request):
    games = Games.objects.all()
    consoles = Consoles.objects.all()
    phones = Phones.objects.all()
    peripherals = Peripherals.objects.all()
    context = {
        'games':games,
        'consoles':consoles,
        'phones':phones,
        'peripherals':peripherals,
    }
    return render(request, 'list_products.html', context = context)

@login_required
def search_product(request):
    search = request.GET['search']
    games = Games.objects.filter(name__icontains=search)
    consoles = Consoles.objects.filter(name__icontains=search) 
    phones = Phones.objects.filter(name__icontains=search)
    peripherals = Peripherals.objects.filter(name__icontains=search) 
    context = {'games':games, 'consoles':consoles, 'phones':phones, 'peripherals':peripherals}
    return render(request, 'search_product.html', context=context)

