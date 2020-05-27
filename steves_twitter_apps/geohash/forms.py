from django import forms
from .models import Woeids


def tuplefy_countries():
    """Query Woeids model for sorted list of countries and reformat into list of tuples
    for consumption by SelectCountry form class.
    """
    q_set = Woeids.objects.values('country').distinct().order_by('country')
    COUNTRIES = []
    for d in q_set:
        for k, v in d.items():
            COUNTRIES.append((v,v))
    return COUNTRIES

def tuplefy_names(country='United States'):
    """Query Woeids model for sorted list of 'names', i.e., metro areas, within the 
    selected country and reformat into list of tuples for consumption by
    SelectMetro class.
    """
    NAMES = []
    q_set = Woeids.objects.filter(country=country).values('name').order_by('name')
    for d in q_set:
        for k, v in d.items():
            NAMES.append((v,v,))
    return NAMES


class SelectCountry(forms.Form):
    country = forms.ChoiceField(widget=forms.Select, choices=tuplefy_countries())

"""STUCK! -- How can I pass a metro area 'name' into SelectMetro such that the
select widget only renders the names of metros returned by tuplefy_names(<metro name>)???
"""

class SelectMetro(forms.Form):
    def __init__(self, country='United States'):
        self.country = country

    metro = forms.ChoiceField(widget=forms.Select, choices=tuplefy_names())
