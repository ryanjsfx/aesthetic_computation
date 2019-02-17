
from django.conf.urls import include, url
from django.contrib import admin

from .views import home, post

urlpatterns = [
    # index
    url(r'^$', home, name='home'),

    # single post
    url(r'^(?P<id>[0-9]+)/$', post, name='post'),

    # admin
    url(r'^admin/', admin.site.urls),

    # category listing (must come last)
    url(r'^(?P<category_name>[A-Za-z0-9]+)/', home, name='category'),
]

handler404 = '.views.handler404'
handler500 = '.views.handler500'
