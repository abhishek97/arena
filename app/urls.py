from django.conf.urls import patterns,url
from views import *

urlpatterns = patterns('',

	url(r'register', RegisterView.as_view() ),

	);