from dal import autocomplete
from django import forms
from .models import Suscription

class SuscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Suscription
        fields = ('event',  'cyclist', 'jersey', 'medal', 'ride', 'size', 'package', 'status')
        widgets = {
            'cyclist': autocomplete.ModelSelect2(url='cyclist-autocomplete')
        }