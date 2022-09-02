from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from Tienda.models import Games, Consoles, Phones, Peripherals
from Tienda.forms import formulario_for_games
from django.views.generic import ListView, DetailView, CreateView, DeleteView   
from django.views.generic.edit import UpdateView

# GAMES

def create_game(request):
    
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

            return redirect(list_games)
        
    elif request.method == 'GET':
        form = formulario_for_games()
        context = {'form':form}
        return render(request, 'games/create_game.html', context=context)
        

def list_games(request):
    games = Games.objects.all()
    context = {
        'games':games
    }
    return render(request, 'games/list_games.html', context = context)

def formulario_games(request):
    print(request.method)
    if request.method == 'POST': 
        print(request.POST)
    return render(request, 'games/formulario_games.html', context={})

def delete_game(request, pk):
    if request.method == 'GET':
        game = Games.objects.get(pk=pk)
        context = {'game':game}
        return render(request, 'games/delete_game.html', context=context)
    
    elif request.method == 'POST':
        game = Games.objects.get(pk=pk)
        game.delete()
        return redirect(list_games)
        

def update_game(request, pk):
    if request.method == 'POST':
        form = formulario_for_games(request.POST)
        if form.is_valid():
            game = Games.objects.get(id=pk)
            game.name = form.cleaned_data['name']
            game.price = form.cleaned_data['price']
            game.stock = form.cleaned_data['stock']
            game.game_company = form.cleaned_data['game_company']
            game.save()
            
            return redirect(list_games)
    
    elif request.method == 'GET':
        game = Games.objects.get(id=pk)
        form = formulario_for_games(initial={
                                        'name':game.name, 
                                        'price':game.price, 
                                        'stock':game.stock, 
                                        'game_company':game.game_company})
        context = {'form':form}
        return render(request, 'games/update_game.html', context=context)





#def create_console(request):
#    create_console = Consoles.objects.create(name='PS4', price = 50000, stock = 10, producer = 'Sony')
#    context = {
#        'create_console':create_console,
#    }
#    return render(request, 'consoles/create_console.html', context=context)

#def list_consoles(request):
#    consoles = Consoles.objects.all()
#    context = {
#        'consoles':consoles
#    }
#    return render(request, 'consoles/list_consoles.html', context = context)

# CONSOLES

class List_consoles(ListView):
    model = Consoles
    template_name = 'consoles/list_consoles.html'
    
class Detaile_console(DetailView):
    model = Consoles
    template_name = 'consoles/detail_console.html'
    
class Create_console(CreateView):
    model = Consoles
    template_name = 'consoles/create_console.html'
    fields = '__all__'
    success_url = '/Tienda/list-consoles/'

class Delete_console(DeleteView):
    model = Consoles
    template_name = 'consoles/delete_console.html'
    success_url = '/Tienda/list-consoles/'        

class Update_console(UpdateView):
    model = Consoles
    template_name = 'consoles/update_console.html'
    fields = '__all__'
    success_url = '/Tienda/list-consoles/' 





# def search_games(request):
#     search = request.GET['search']
#     games = Games.objects.filter(name__icontains=search)
#     context = {'games':games}
#     return render(request, 'games/search_games.html', context=context)


#PHONES


class List_phones(ListView):
    model = Phones 
    template_name = 'phones/list_phones.html'
    
class Detaile_phone(DetailView):
    model = Phones
    template_name = 'phones/detail_phone.html'
    
class Create_phone(CreateView):
    model = Phones
    template_name = 'phones/create_phone.html'
    fields = '__all__'
    success_url = '/Tienda/list-phones/'

class Delete_phone(DeleteView):
    model = Phones
    template_name = 'phones/delete_phone.html'
    success_url = '/Tienda/list-phones/'        

class Update_phone(UpdateView):
    model = Phones
    template_name = 'phones/update_phone.html'
    fields = '__all__'
    success_url = '/Tienda/list-phones/' 




# PERIPHERALS


class List_peripherals(ListView):
    model = Peripherals
    template_name = 'peripherals/list_peripherals.html'
    
class Detaile_peripheral(DetailView):
    model = Peripherals
    template_name = 'peripherals/detail_peripheral.html'
    
class Create_peripheral(CreateView):
    model = Peripherals
    template_name = 'peripherals/create_peripheral.html'
    fields = '__all__'
    success_url = '/Tienda/list-peripherals/'

class Delete_peripheral(DeleteView):
    model = Peripherals
    template_name = 'peripherals/delete_peripheral.html'
    success_url = '/Tienda/list-peripherals/'        

class Update_peripheral(UpdateView):
    model = Peripherals
    template_name = 'peripherals/delete_peripheral.html'
    fields = '__all__'
    success_url = '/Tienda/list-peripherals/'




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

def search_product(request):
    search = request.GET['search']
    games = Games.objects.filter(name__icontains=search)
    consoles = Consoles.objects.filter(name__icontains=search) 
    phones = Phones.objects.filter(name__icontains=search)
    peripherals = Peripherals.objects.filter(name__icontains=search) 
    context = {'games':games, 'consoles':consoles, 'phones':phones, 'peripherals':peripherals}
    return render(request, 'search_product.html', context=context)