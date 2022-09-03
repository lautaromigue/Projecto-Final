from django.shortcuts import render
from blog.models import Article




def create_article(request):
    new_article = Article.objects.create(title = "GameStop: Nuestro proyecto final", description = "Proyecto final del curso de python. Creamos un e-commers intuitivo y funcional en donde se puede administrar la pagina creando y modificando los diferentes productos a traves de las herramientas ofrecidas por el framework Django", authors = "Lautaro Miguel y Lautaro Alvarez Nogueira")
    context = {"new_article":new_article}
    return render(request, "create_article.html", context=context)   