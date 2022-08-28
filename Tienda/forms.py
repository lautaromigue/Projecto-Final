from django import forms

class formulario_for_games(forms.Form):
    name = forms.CharField(max_length=150)
    price = forms.FloatField()
    stock = forms.IntegerField()
    game_company = forms.CharField(max_length=100)
    image = forms.ImageField()
    
class formulario_for_consoles(forms.Form):
    name = forms.CharField(max_length=150)
    price = forms.FloatField()
    stock = forms.IntegerField()
    producer = forms.CharField(max_length=100)
    image = forms.ImageField()


class formulario_for_phones(forms.Form):
    name = forms.CharField(max_length=150)
    price = forms.FloatField()
    stock = forms.IntegerField()
    producer = forms.CharField(max_length=100)
    image = forms.ImageField()


class formulario_for_peripherals(forms.Form):
    name = forms.CharField(max_length=150)
    price = forms.FloatField()
    stock = forms.IntegerField()
    producer = forms.CharField(max_length=100)
    image = forms.ImageField()

    