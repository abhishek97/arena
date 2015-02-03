from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from forms import RegisterForm , LoginForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate , login , logout


class RegisterView(View):

	def get(self,request):
		form = RegisterForm()
		return render(request, 'register.html' , { 'form' : form  } )

	def post(self,request):

		form = RegisterForm(request.POST)
		
		if form.is_valid() :
			this = form.cleaned_data

			if this.get('Email') != this.get('CEmail') :
				return render(request , 'register.html' , { 'form' : RegisterForm() , 'error' : 'Emails Doesnot Match!' } )

			if this.get('Password') != this.get('CPassword') :
				return render(request , 'register.html' , { 'form' : RegisterForm(this) , 'error' : "Passwords Don't Match!" } )

			try :
				user = User.objects.create_user(this.get('Username') , this.get('Email') , this.get('Password') )
			except IntegrityError :
				return render(request , 'register.html' , { 'form' : RegisterForm() , 'error' : 'The UserName Already exists!' } )

			user.first_name = this.get('FirstName')
			user.last_name = this.get('LastName')
			user.save()

			return render(request , 'registered.html' , { 'user' : user } )


		else:
			newForm = RegisterForm()
			return render(request , 'register.html' , { 'form' : newForm , 'error' : 'Invalid Data' } )


class LoginView(View):
	def get(self,request):
		newForm = LoginForm()
		return render(request , 'login.html' , { 'form' : newForm } )

	def post(self, request):
		form = LoginForm(request.POST)

		if form.is_valid() :
			this = form.cleaned_data
			user = authenticate(username=this.get('Username') ,password =this.get('Password') )

			if user is not None :
				login(request , user);
				return render(request , 'logged.html' , {'user' : user} )
			else :
				return render(request , 'login.html' , {'form' : LoginForm() , 'error' : 'Invalid Username/Password Combination'} )
		else :
			return render(request , 'login.html' , {'form' : form ,'error' : 'Invalid Username/Password Combination'} )



class LogoutView(View):
	def get(self,request):
		logout(request)
		return render(request , 'logout.html' )
