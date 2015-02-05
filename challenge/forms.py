from django import forms


class CreateForm(forms.Form):
	to = forms.CharField(label='You Challenge' , max_length=50)
	contest = forms.CharField(label='For the Contest' , max_length=50)


class FilterForm(forms.Form):
	frm = forms.CharField(label='From ',max_length=100, required=False )
	contest = forms.CharField(label='For Contest ', max_length=50 , required=False)
	resolved = forms.BooleanField(label='Accepted ',required=False)


class AcceptForm(forms.Form):
	to = forms.CharField(max_length=50)
	frm = forms.CharField(max_length=50)
	contest = forms.CharField(max_length=50)


