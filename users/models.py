from distutils.command.upload import upload
from email.mime import image
from unicodedata import name
from django.db import models

class User_profile(models.Model):
    name = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=400, blank=True)
    website = models.CharField(max_length=300, blank=True,null=True)
    image = models.ImageField(upload_to = "profile_images/", blank=True)

    def __str__(self):
        return self.user.username + " - profile"