from django import forms

class customerform(forms.Form):
    email=forms.EmailField()
    name=forms.CharField(max_length=200)
    message=forms.CharField(max_length=1000)