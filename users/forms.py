from django import forms
from users.models import Usuario


class Login(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'id' :"user", 'type':"text", 'required': "",
	'maxlength': "30", 'onkeyup': "nospaces(this)"}), required=True);
	password = forms.CharField(widget=forms.TextInput(attrs={'id' :"password", 'type':"text", 'required': "",
	'maxlength': "30", 'onkeyup': "nospaces(this)"}), required=True)
	class Meta:
		model = Usuario;
		fields = ['user','password']



class Signup(forms.ModelForm):
	user = forms.CharField(widget=forms.TextInput(attrs={'id':"ruser", 'type':"text" , 'maxlength':"10"
		, 'onkeyup':"nospaces(this)"}), required=True);
	password = forms.CharField(widget=forms.TextInput(attrs={'id':"password", 'type':"text" , 'maxlength':"10"
		, 'onkeyup':"nospaces(this)"}), required=True);
	class Meta:
		model = Usuario;
		fields = ['user','password']
