from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),
   
    url(r'admin/', include(admin.site.urls)),
    url(r'account/', include('account.urls')  ),
    url(r'challenge/', include('challenge.urls') ),
    url(r'^$', views.IndexView.as_view(), name='home'),
)
