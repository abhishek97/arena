from django import forms


class CreateForm(forms.Form):
	to = forms.CharField(label='You Challenge' , max_length=50)
	contest = forms.CharField(label='For the Contest' , max_length=50)
	
