from django.conf.urls.defaults import *

urlpatterns = patterns('wonderwar',
    (r'^new_text/(\d+)/$', 'views.new_text'),
    (r'^new_text/?$', 'views.new_text'),
    (r'^$', 'views.index'),
)
