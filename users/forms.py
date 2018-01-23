from django import forms


class Login(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'id' :"user", 'type':"text", 'required': "",
	'maxlength': "10", 'onkeyup': "nospaces(this)"}), required=True);
	password = forms.CharField(widget=forms.TextInput(attrs={'id' :"password", 'type':"text", 'required': "",
	'maxlength': "10", 'onkeyup': "nospaces(this)"}), required=True)


class Signup(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'id':"ruser", 'type':"text" , 'maxlength':"10"
		, 'onkeyup':"nospaces(this)"}), required=True)
	password = forms.CharField(widget=forms.TextInput(attrs={'id':"password", 'type':"text" , 'maxlength':"10"
		, 'onkeyup':"nospaces(this)"}), required=True)
