from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qpgen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','basic.views.login_user',name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^qpdetail/?','basic.views.qpdetail',name='qpdetail'),
    url(r'^logout/?','basic.views.logout_user',name='logout'),
    url(r'^contact/?','basic.views.contact',name='contact'),
    url(r'^about/?','basic.views.about',name='about'),
   # url(r'^subject_jsons/',,)

)
