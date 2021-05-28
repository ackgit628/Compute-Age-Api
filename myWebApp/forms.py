from django import forms

class AgeForm(forms.Form):
    day = forms.IntegerField()
    month = forms.IntegerField()
    year = forms.IntegerField()