from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'clothes.views.home'),
    (r'^results/$', 'clothes.views.results'),
	(r'^product_info/$', 'clothes.views.product_info'),
	# url(r'^clothesliner/', include('clothesliner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
