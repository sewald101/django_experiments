from django import forms
from .models import Woeids

q_set = Woeids.objects.values('country').distinct().order_by('country')
COUNTRIES = []
for d in q_set:
    for k, v in d.items():
        COUNTRIES.append((v,v))

"""
FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
"""

class SelectCountry(forms.Form):
    country = forms.ChoiceField(widget=forms.Select, choices=COUNTRIES)
