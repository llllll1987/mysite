from django.conf.urls import patterns, include, url
from mysite.views import hello,current_datetime,base
from django.contrib import admin
# from myblog.views import blog_list,search_form,search
from myblog.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^bloglist/$',blog_list,name = 'bloglist'),
    url(r'^base/$',base),
    url(r'^searchform/$',search_form,name = 'searchform'),
    url(r'^search/$',search),
)
