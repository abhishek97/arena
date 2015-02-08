from django.conf.urls import url,patterns
from views import *

urlpatterns = patterns('/',

	url(r'create', CreateView.as_view() ),
	url(r'all', AllView.as_view() ),
	url(r'accept', AcceptView.as_view() ),
	url(r'notification', NotificationView.as_view()),
	

	)