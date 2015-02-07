from django.shortcuts import render , HttpResponseRedirect
from django.views.generic import View
from forms import CreateForm , FilterForm , AcceptForm
from models import Challenge , Contest , Notification
from datetime import datetime
from django.db import InternalError,IntegrityError
from django.contrib.auth.models import User

class CreateView(View):

	def get(self, request):
		if not request.user.is_authenticated() :
			return render(request , 'unauthorised.html' )
		
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

			#Create a New Notification
			try:
				notif  = Notification.objects.create(user=this.get('to'),title='You have been challenged by ' + request.user.username )
			except (InternalError):
				return render(request ,  'create_challenge.html' , { 'form' : form , 'error' : 'Internal Server Error 500, Please try again.' } )

			return render(request , 'created_challenge.html' , { 'challenge' : ch , 'contest' : con } )


		else :
			return render(request ,  'create_challenge.html' , { 'form' : CreateForm() , 'error' : 'Invalid Form Data' } )
 

class AllView(View):

	def get(self,request):

		if not request.user.is_authenticated():
			return render(request , 'unauthorised.html' )

		q_set = Challenge.objects.filter(to=request.user.username,resolved=False).order_by('-time')

		return render(request , 'show_challenge.html' , {'form' : FilterForm() , 'results' : q_set })

	def post(self,request):

		if not request.user.is_authenticated():
			return render(request , 'unauthorised.html' )

		form = FilterForm(request.POST)

		if not form.is_valid():
			return render(request, 'show_challenge.html' , {'form' :  form , 'error' : 'Invalid Form Data'} )

		this = form.cleaned_data
		q_set = Challenge.objects.filter(to=request.user.username,resolved=this.get('resolved')).order_by('-time')

		if this.get('frm') != '' :
			q_set = q_set.filter(frm=this.get('frm'))

		if this.get('contest') != '' :
			q_set = q_set.filter(contest=this.get('contest'))

		if len(q_set):
			return render(request , 'show_challenge.html' , {'form' : form , 'results' : q_set } )

		else:
			return render(request , 'show_challenge.html' , {'form': form , 'error' : 'No search items found matching the required filters'} )


class AcceptView(View):

	def post(self,request):

		if not request.user.is_authenticated():
			return render(request , 'unauthorised.html' )

		form = AcceptForm(request.POST)

		if not form.is_valid():
			return render(request , '500.html')

		this = form.cleaned_data
		obj  = Challenge.objects.filter(to=request.user.username,frm=this.get('frm'),contest=this.get('contest')).order_by('-time')

		if len(obj) :
			obj[0].resolved = True
			#Create a New Notification
			try :
				obj[0].save()
				notif  = Notification.objects.create(user=this.get('frm'),title='Your Challenge is accepted by ' + request.user.username )
			except(InternalError):
				render(request , 'show_challenge.html' , {'form' : FilterForm() , 'error' : 'Internal Server Error' } )
		else :
			render(request , 'show_challenge.html' , {'form' : FilterForm() , 'error' : 'Internal Server Error' } )
		
		return HttpResponseRedirect('/challenge/all')

class NotificationView(View):

	def get(self,request):
		
		if not request.user.is_authenticated():
			return render(request , 'unauthorised.html' )

		q_set = Notification.objects.filter(user=request.user.username)
		if len(q_set):
			return render(request , 'show_notification.html' , {'notifications' : q_set } )	
		else :
			return render(request , 'show_notification.html' , {'error' : 'No Notifications' } )	
