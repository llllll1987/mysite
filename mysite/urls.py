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
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': '/Users/gefli/www/djcode/mysite/mysite/templates/static/media/js/' }),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/gefli/www/djcode/mysite/mysite/templates/static/media/css/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^$',base),
    url(r'^bloglist/$',blog_list,name = 'bloglist'),
    url(r'^base/$',base),
    url(r'^searchform/$',search_form,name = 'searchform'),
    url(r'^search/$',search),
    url(r'^zhiwei_board_list/$',zhiwei_board_list,name = 'zhiwei_board_list'),
    url(r'^board_tracking/$',board_tracking,name = 'board_tracking'),
    url(r'^sfp_tracking/$',sfp_tracking,name = 'sfp_tracking'),

)
