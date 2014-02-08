from django.conf import settings
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from social.backends.google import GooglePlusAuth

def home(request):
	""" Home view, display login mechanism """
	if request.user.is_authenticated():
		return redirect('done')
	return render_to_response('home.html', {
		'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)
		}, RequestContext(request))

def logout(request):
	""" Logs out User """
	auth_logout(request)
	return render_to_response('home', {}, RequestContext(request))

@login_required
def done(request):
	""" Login complete view, displays user data """
	scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
	return render_to_response('done.html', {
		'user' : request.user,
		'plus_id' : getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
		'plus_scope' : scope
		}, RequestContext(request))