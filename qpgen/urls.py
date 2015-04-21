from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    #Login and logout
    url(r'^$','basic.views.login_user',name='login'),
    url(r'^logout/?','basic.views.logout_user',name='logout'),

    #Create and view question paper
    url(r'^create/?','basic.views.create_qp',name='create_qp'),
    url(r'^view/(?P<qp_id>\d+)/?','basic.views.view_qp',name='view_qp'),

    #Other pages
    url(r'^about/?','basic.views.about',name='about'),
    url(r'^contact/?','basic.views.contact',name='contact'),

)
