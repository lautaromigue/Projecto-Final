from django.contrib import admin
from django.urls import path, include
from Projecto.views import index

from django.conf.urls.static import static
from django.conf import settings
from blog.views import create_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Tienda/', include('Tienda.urls')),
    path('', index, name='index'),
    path('users/', include('users.urls')),
    path("create-article/", create_article, name="create_article")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
