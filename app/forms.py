from django import forms

class RegisterForm(forms.Form):
	FirstName = forms.CharField(label='Frist Name' ,max_length=100)
	LastName = forms.CharField(label='Last Name',max_length=100)
	Username = forms.CharField(label='Your preffered Username',max_length=100)
	Password = forms.CharField(widget=forms.PasswordInput())
	CPassword = forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
	Email = forms.EmailField()
	CEmail = forms.EmailField(label='Confirm Email')
