from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from forms import RegisterForm
from django.contrib.auth.models import User
from django.db import IntegrityError


class RegisterView(View):

	def get(self,request):
		form = RegisterForm()
		return render(request, 'register.html' , { 'form' : form  } )

	def post(self,request):

		form = RegisterForm(request.POST)
		
		if form.is_valid() :
			this = form.cleaned_data
			try :
				user = User.objects.create_user(this.get('Username') , this.get('Email') , this.get('Password') )
			except IntegrityError :
				return render(request , 'register.html' , { 'form' : RegisterForm() , 'error' : 'Invalid Data' } )

			user.first_name = this.get('FirstName')
			user.last_name = this.get('LastName')
			user.save()

			return render(request , 'registered.html' , { 'user' : user } )


		else:
			newForm = RegisterForm()
			return render(request , 'register.html' , { 'form' : newForm , 'error' : 'Invalid Data' } )



# Create your views here.
