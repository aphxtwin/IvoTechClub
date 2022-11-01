
from django import forms

class contactForm(forms.Form):
    email = forms.CharField(label="Email", widget= forms.Textarea(attrs={'cols':25, 'rows': 1, 'style': 'resize:none'}))
    message = forms.CharField(widget = forms.Textarea(attrs={'cols': 25, 'rows': 8, 'style':'resize:none'}))
