from django import forms


class PlaceForm(forms.Form):
    city = forms.CharField(label='city', max_length=50)
