from django import forms

class TextForm(forms.Form):
    text = forms.CharField(max_length = 150, required = True,
                           widget = forms.TextInput(attrs = {'placeholder': 'Enter text'}))