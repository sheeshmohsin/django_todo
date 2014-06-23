from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def home(request):
	if request.user.is_authenticated():
		print request.user.username
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return render_to_response('home.html')