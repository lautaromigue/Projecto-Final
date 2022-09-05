from cmath import log
from django.urls import path
from users.views import login_request, register, my_profile, delete_profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path ("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("my-profile/", my_profile, name="my_profile"),
    path("delete-profile/", delete_profile, name="delete_profile")
    
]