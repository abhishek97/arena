from django.conf.urls import url,patterns
from views import *

urlpatterns = patterns('/',

	url(r'create', CreateView.as_view() )
	)