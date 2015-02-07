from django.db import models
from datetime import datetime

class Challenge(models.Model):
	def __str__(self):
		return self.frm + ' To:  ' + self.to + ' On: ' + self.contest 
		
	frm = models.CharField(max_length=50)
	to  = models.CharField(max_length=50)
	contest = models.CharField(max_length=50)
	resolved = models.BooleanField(default=False)
	expire = models.DateTimeField()
	time = models.DateTimeField()

	
class Contest(models.Model):

	def __str__(self):
		return self.code

	title = models.CharField(max_length=300 , default='')
	code  = models.CharField(max_length=50 , default='A unique code here' , unique=True)
	content = models.TextField(default='')
	url = models.CharField(max_length=1000 , default='')
	start = models.DateTimeField(default=datetime.now())
	end   = models.DateTimeField(default=datetime.now())

class Notification(models.Model):

	def __str__(self):
		return self.user + ' : ' + self.title 

	#TODO : Add more context to Notification regarding what it is about and build content var
	user = models.CharField(max_length=50)
	seen = models.BooleanField(default=False)
	content = models.TextField(default='')
	title = models.CharField(max_length=300)
	time  = models.DateTimeField(default=datetime.now())
