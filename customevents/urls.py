from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.organization import urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'customevents.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.organization.urls')),
]

