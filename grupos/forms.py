from django import forms

class invit(forms.Form):
	grupo = forms.CharField(widget=forms.TextInput(), required=True);
	usuario = forms.CharField(widget=forms.TextInput(),required=True)
