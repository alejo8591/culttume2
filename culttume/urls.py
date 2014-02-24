from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'culttume.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Migrating function-based generic views - https://docs.djangoproject.com/en/1.4/topics/generic-views-migration/
    #url(r'^admin/', include(account.views.home)),
    url(r'^$', 'accounts.views.home'),
    url(r'^login/$', 'accounts.views.home'),
    url(r'^logout/$', 'accounts.views.logout'),
    url(r'^done/$', 'accounts.views.done', name='done'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
)