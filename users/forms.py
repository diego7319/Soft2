from django import forms
from django.forms import ModelForm, TextInput


class Login(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}), required=True)


class Registro(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
                               required=True)
