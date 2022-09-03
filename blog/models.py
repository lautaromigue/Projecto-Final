from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    creation_date = models.DateField(auto_now_add=True)
    authors = models.CharField(max_length=100)
