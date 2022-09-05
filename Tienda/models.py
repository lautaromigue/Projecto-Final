from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from django.db import models

class Games(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    stock = models.IntegerField()
    game_company = models.CharField(max_length=100)
    image = models.ImageField(upload_to='game_images/', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
    

class Consoles(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    producer = models.CharField(max_length=100)
    image = models.ImageField(upload_to='console_images/', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Console'
        verbose_name_plural = 'Consoles'
    
class Phones(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    producer = models.CharField(max_length=100)
    image = models.ImageField(upload_to='phone_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
        
    
class Peripherals(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    producer = models.CharField(max_length=100)
    image = models.ImageField(upload_to='peripheral_images/', blank=True)     

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Peripheral'
        verbose_name_plural = 'Peripherals'  



