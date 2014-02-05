from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'culttume.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Migrating function-based generic views - https://docs.djangoproject.com/en/1.4/topics/generic-views-migration/
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^login/$', RedirectView, {'url': '/login/facebook'}),
    #url(r'^private/$', 'home.views.private'),
)