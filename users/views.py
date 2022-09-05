from http.client import HTTPResponse
from multiprocessing import AuthenticationError, context
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm 

from .forms import UserEditForm

from django.contrib.auth import login, logout, authenticate 
from users.forms import User_registration_form, Edit_profile_form
from users.models import User_profile

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                context = {'message':f'Bienvenido {username}'}
                return render(request, 'index.html', context=context)
            
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulario inválido', 'form': form})
    
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:    
            context = {"errors":form.errors}
            form = User_registration_form()
            context["form"] = form
            return render(request, "users/register.html", {"form":form})

    elif request.method =='GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form':form})
    


def show_profile(request):
   if request.user.is_authenticated:
    return HttpResponse(request.user.profile)  


    
@login_required
def profile(request):    
    if request.user.is_authenticated:                                                   
        try:            
            user = User_profile.objects.get(user=request.user)
        except:            
            user = User_profile.objects.create(user=request.user)
        user.save()     
    if request.method == "POST":                 
            form = Edit_profile_form(request.POST, request.FILES) 
              
            if form.is_valid():                                                             
                user.user = form.cleaned_data['user']                           
                user.address = form.cleaned_data ['address']
                user.phone = form.cleaned_data['phone']
                user.description = form.cleaned_data['description']
                
                if form.cleaned_data['image'] != None:
                    user.image = form.cleaned_data['image']
                
                user.website = form.cleaned_data['website']
                user.save()    
                context = {'form':form,'user':user}             
                return render(request, 'users/profile.html', context=context)
            
    elif request.method == "GET":                 
            form = Edit_profile_form(initial = {
                            'user':user.user,
                            'address':user.address,
                            'phone':user.phone,
                            'description':user.description,
                            'image': user.image,
                            'website':user.website,                           
                                    })
            context = {'form':form,'user':user}    
            return render(request, 'users/profile.html', context=context)
    return redirect ("index")


@login_required
def delete_profile(request):                       
    if request.user.is_authenticated:
        if request.method == 'GET':            
            user_profile = User_profile.objects.get(user=request.user)  
            context = {'userProfile':user_profile}
            return render(request, 'users/delete_profile.html', context=context)     
        elif request.method == 'POST':
            user_profile = User_profile.objects.get(user=request.user)
            user_profile.delete()
            request.user.delete()           
    return redirect('login')            
