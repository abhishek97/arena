from django import forms

class RegisterForm(forms.Form):
	FirstName = forms.CharField(max_length=100)
	LastName = forms.CharField(max_length=100)
	Username = forms.CharField(max_length=100)
	Password = forms.CharField(widget=forms.PasswordInput())
	CPassword = forms.CharField(widget=forms.PasswordInput())
	Email = forms.EmailField()
	CEmail = forms.EmailField()
