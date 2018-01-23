from django import forms


class Login(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'id' :"user", 'type':"text", 'required': "",
	'maxlength': "30", 'onkeyup': "nospaces(this)"}), required=True);
	password = forms.CharField(widget=forms.TextInput(attrs={'id' :"password", 'type':"text", 'required': "",
	'maxlength': "30", 'onkeyup': "nospaces(this)"}), required=True)


class Signup(forms.Form):

	user = forms.CharField(widget=forms.TextInput(attrs={'id':"ruser", 'type':"text" , 'maxlength':"10"
		, 'onkeyup':"nospaces(this)"}), required=True);
	password = forms.CharField(widget=forms.TextInput(attrs={'id':"password", 'type':"text" , 'maxlength':"10"
		, 'onkeyup':"nospaces(this)"}), required=True);

	def save(self, commit=True):
		instance = super(Usuario, self).save(commit=False);
		instance.user= self.user;
		instance.password = self.password;
		if commit:
			instance.save();
		return instance
