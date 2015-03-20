from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import quick_test,home,help,about

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learning_lettuce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quick-test/$', quick_test),
    url(r'^home/$', home),
    url(r'^help/$', help),
    url(r'^about/$', about),
)


