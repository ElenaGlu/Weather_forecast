from django import forms


class PlaceForm(forms.Form):
    place = forms.CharField(label='place', max_length=100)