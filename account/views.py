from django.conf import settings
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from social.backends.google import GooglePlusAuth

from social.backends.facebook import FacebookOAuth2

def home(request):
	""" Home view, display login mechanism """
	if request.user.is_authenticated():
		return redirect('done')
	return render_to_response('home.html', {
		'appId': getattr(settings, 'SOCIAL_AUTH_FACEBOOK_KEY', None)
		}, RequestContext(request))

def logout(request):
	""" Logs out User """
	auth_logout(request)
	return render_to_response('home', {}, RequestContext(request))

@login_required
def done(request):
	""" Login complete view, displays user data """
	scope = ' '.join(FacebookOAuth2.DEFAULT_SCOPE)
	return render_to_response('done.html', {
		'appId' : getattr(settings, 'SOCIAL_AUTH_FACEBOOK_KEY', None),
		}, RequestContext(request))