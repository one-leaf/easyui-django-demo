from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from settings import HERE

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'easyoa.oa.views.index',),
    url(r'^resources/(?P<path>.*)$', 'django.views.static.serve',{'document_root': HERE+'/htdocs/resources/'}),
    url(r'^menu/getAccordionItem$', 'easyoa.oa.views.getAccordionItem'),
    url(r'^menu/getAllTreeNode/(?P<parentId>.*)$', 'easyoa.oa.views.getAllTreeNode'),
    url(r'^department/$','easyoa.oa.views.department'),
    url(r'^department/(?P<action>.*)$','easyoa.oa.views.departmentAction'),
    url(r'^aclUser/$','easyoa.oa.views.aclUser'),
    url(r'^aclUser/(?P<action>.*)$','easyoa.oa.views.aclUserAction'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
