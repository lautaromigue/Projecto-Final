from http.client import HTTPResponse
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from re import search
from Tienda.models import Games, Consoles, Phones, Peripherals
from Tienda.forms import formulario_for_consoles, formulario_for_games, formulario_for_phones, formulario_for_peripherals

from django.views.generic import DetailView
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
        print('estoy aca')
        if request.method == 'POST':
            print('estoy aca 2')
            form = formulario_for_games(request.POST, request.FILES)
            print(form.errors)
            if form.is_valid():
                print('estoy aca 3')
                game = Games.objects.get(id=pk)
                game.name = form.cleaned_data['name']
                game.price = form.cleaned_data['price']
                game.stock = form.cleaned_data['stock']
                game.game_company = form.cleaned_data['game_company']

                if form.cleaned_data['image'] !=None:
                    game.image = form.cleaned_data['image']
                print(game)
                game.save()
                
            return redirect(list_products)
        
        elif request.method == 'GET':
            print('estoy aca 4')
            game = Games.objects.get(id=pk)
            form = formulario_for_games(initial={
                                            'name':game.name, 
                                            'price':game.price, 
                                            'stock':game.stock, 
                                            'game_company':game.game_company,
                                            'image':game.image})
            context = {'form':form}
            return render(request, 'games/update_game.html', context=context)
    return redirect ("login")           


class Detail_game(DetailView):
    model = Games
    template_name = 'games/detail_game.html'


#CONSOLES
    


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
        print('estoy aca')
        if request.method == 'POST':
            print('estoy aca 2')
            form = formulario_for_consoles(request.POST, request.FILES)
            print(form.errors)
            if form.is_valid():
                print('estoy aca 3')
                console = Consoles.objects.get(id=pk)
                console.name = form.cleaned_data['name']
                console.price = form.cleaned_data['price']
                console.stock = form.cleaned_data['stock']
                console.producer = form.cleaned_data['producer']

                if form.cleaned_data['image'] !=None:
                    console.image = form.cleaned_data['image']
                print(console)
                console.save()
                
            return redirect(list_products)
        
        elif request.method == 'GET':
            print('estoy aca 4')
            console = Consoles.objects.get(id=pk)
            form = formulario_for_consoles(initial={
                                            'name':console.name, 
                                            'price':console.price, 
                                            'stock':console.stock, 
                                            'producer':console.producer,
                                            'image':console.image})
            context = {'form':form}
            return render(request, 'consoles/update_console.html', context=context)
    return redirect ("login") 


class Detail_console(DetailView):
    model = Consoles
    template_name = 'consoles/detail_console.html'






#PHONES

    
    
    
@login_required
def create_phone(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = formulario_for_phones(request.POST, request.FILES)
            
            if form.is_valid():
                Phones.objects.create(
                    name = form.cleaned_data['name'],
                    price = form.cleaned_data['price'],
                    stock = form.cleaned_data['stock'],
                    producer = form.cleaned_data['producer'],
                    image = form.cleaned_data['image'],
                )

            return redirect(list_products)
            
        elif request.method == 'GET':
            form = formulario_for_phones()
            context = {'form':form}
            return render(request, 'phones/create_phone.html', context=context)
    return redirect ("login")    
 


@login_required
def list_phones(request):
    phones = Phones.objects.all()
    context = {
        'phones':phones
    }
    return render(request, 'phones/list_phones.html', context = context)



@login_required
def formulario_phones(request):
    print(request.method)
    if request.method == 'POST': 
        print(request.POST)
    return render(request, 'phones/formulario_phones.html', context={})



@login_required
def delete_phone(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
                phone = Phones.objects.get(pk=pk)
                context = {'phone':phone}
                return render(request, 'phones/delete_phone.html', context=context)
        
        elif request.method == 'POST':
                console = Phones.objects.get(pk=pk)
                console.delete()
                return redirect(list_products)
    return redirect ("login")        



@login_required
def update_phone(request, pk):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = formulario_for_phones(request.POST, request.FILES)
            if form.is_valid():
                phone = Phones.objects.get(id=pk)
                phone.name = form.cleaned_data['name']
                phone.price = form.cleaned_data['price']
                phone.stock = form.cleaned_data['stock']
                phone.producer = form.cleaned_data['producer']
                
                if form.cleaned_data['image'] !=None:
                    phone.image = form.cleaned_data['image']
                print(phone)
                phone.save()
                phone.save()
                
            return redirect(list_products)
        
        elif request.method == 'GET':
            phone = Phones.objects.get(id=pk)
            form = formulario_for_phones(initial={
                                            'name':phone.name, 
                                            'price':phone.price, 
                                            'stock':phone.stock, 
                                            'producer':phone.producer,
                                            'image':phone.image})
            context = {'form':form}
            return render(request, 'phones/update_phone.html', context=context)
    return redirect ("login")  


class Detaile_phone(LoginRequiredMixin,DetailView):
    model = Phones
    template_name = 'phones/detail_phone.html'




# PERIPHERALS

    
    
@login_required
def create_peripheral(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = formulario_for_peripherals(request.POST, request.FILES)
            
            if form.is_valid():
                Peripherals.objects.create(
                    name = form.cleaned_data['name'],
                    price = form.cleaned_data['price'],
                    stock = form.cleaned_data['stock'],
                    producer = form.cleaned_data['producer'],
                    image = form.cleaned_data['image'],
                )

            return redirect(list_products)
            
        elif request.method == 'GET':
            form = formulario_for_peripherals()
            context = {'form':form}
            return render(request, 'peripherals/create_peripheral.html', context=context)
    return redirect ("login")    
 


@login_required
def list_peripherals(request):
    peripherals = Peripherals.objects.all()
    context = {
        'peripherals':peripherals
    }
    return render(request, 'peripherals/list_peripherals.html', context = context)



@login_required
def formulario_peripherals(request):
    print(request.method)
    if request.method == 'POST': 
        print(request.POST)
    return render(request, 'peripherals/formulario_peripherals.html', context={})



@login_required
def delete_peripheral(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
                peripheral = Peripherals.objects.get(pk=pk)
                context = {'peripheral':peripheral}
                return render(request, 'peripherals/delete_peripheral.html', context=context)
        
        elif request.method == 'POST':
                peripheral = Peripherals.objects.get(pk=pk)
                peripheral.delete()
                return redirect(list_products)
    return redirect ("login")        



@login_required
def update_peripheral(request, pk):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = formulario_for_peripherals(request.POST, request.FILES)
            if form.is_valid():
                peripheral = Peripherals.objects.get(id=pk)
                peripheral.name = form.cleaned_data['name']
                peripheral.price = form.cleaned_data['price']
                peripheral.stock = form.cleaned_data['stock']
                peripheral.producer = form.cleaned_data['producer']
                
                if form.cleaned_data['image'] !=None:
                    peripheral.image = form.cleaned_data['image']
                print(peripheral)
                peripheral.save()
                
            return redirect(list_products)
        
        elif request.method == 'GET':
            peripheral = Peripherals.objects.get(id=pk)
            form = formulario_for_peripherals(initial={
                                            'name':peripheral.name, 
                                            'price':peripheral.price, 
                                            'stock':peripheral.stock, 
                                            'producer':peripheral.producer,
                                            'image':peripheral.image})
            context = {'form':form}
            return render(request, 'peripherals/update_peripheral.html', context=context)
    return redirect ("login")     
    
    
class Detaile_peripheral(LoginRequiredMixin,DetailView):
    model = Peripherals
    template_name = 'peripherals/detail_peripheral.html'    
    





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

