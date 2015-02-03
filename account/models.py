from django.db import models

class Challenge(models.Model):
	frm = models.CharField(max_length=50)
	to  = models.CharField(max_length=50)
	contest = models.CharField(max_length=50)
	resolved = models.BooleanField(default=False)
	expire = models.DateTimeField()
	time = models.DateTimeField()
