from django.shortcuts import render
from django.views.generic import View
from forms import CreateForm
from models import Challenge , Contest
from datetime import datetime
from django.db import InternalError,IntegrityError
from django.contrib.auth.models import User


class CreateView(View):

	def get(self, request):

		form = CreateForm()
		return render(request , 'create_challenge.html' , { 'form' : form })

	def post(self , request):

		if not request.user.is_authenticated() :
			return render(request , 'unauthorised.html' )
		
		form = CreateForm(request.POST)

		if form.is_valid() :
			
			this = form.cleaned_data
			q_con  = Contest.objects.filter(code=this.get('contest'))
			q_user = User.objects.filter(username=this.get('to')) 

			if len(q_con)==0 :
				return render(request ,  'create_challenge.html' , { 'form' : form , 'error' : 'Contest Code is incorrect,Please make sure the contest is still active' } )

			if len(q_user)==0:
				return render(request , 'create_challenge.html' , { 'form' : CreateForm() , 'error' : 'No User with that username found.' } )

			try:
				con = q_con[0]  
				ch   = Challenge.objects.create(frm=request.user.username,to=this.get('to'),contest=con.code,expire=con.end,time=datetime.now())
			except (InternalError,IntegrityError):
				return render(request ,  'create_challenge.html' , { 'form' : form , 'error' : 'Internal Server Error 500, Please try again.' } )

			return render(request , 'created_challenge.html' , { 'challenge' : ch , 'contest' : con } )


		else :
			return render(request ,  'create_challenge.html' , { 'form' : CreateForm() , 'error' : 'Invalid Form Data' } )
 









