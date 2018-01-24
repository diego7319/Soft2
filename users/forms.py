from django import forms
from users.models import Usuario
from django.contrib.auth.models import User

class Login(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'id' :"user", 'type':"text", 'required': "",
	'maxlength': "30", 'onkeyup': "nospaces(this)"}), required=True);
	password = forms.CharField(widget=forms.TextInput(attrs={'id' :"password", 'type':"text", 'required': "",
	'maxlength': "30", 'onkeyup': "nospaces(this)"}), required=True)
	class Meta:
		model = User
		fields = "__all__"


class Signup(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'id':"ruser", 'type':"text" , 'maxlength':"10"
	, 'onkeyup':"nospaces(this)",'maxlength': "30"}), required=True);
	password = forms.CharField(widget=forms.TextInput(attrs={'id':"password", 'type':"text" , 'maxlength':"10"
	, 'onkeyup':"nospaces(this)",'maxlength': "30"}), required=True);
	class Meta:
		model = User
		fields = "__all__"
