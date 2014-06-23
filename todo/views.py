from django.contrib import auth
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

@login_required
def loggedin(request):
	tasks = request.user.todolist_set.all()
	return render_to_response('loggedin.html', {'full_name':request.user.username, 'tasks':tasks}, context_instance=RequestContext(request))

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/accounts/register_success/')
			else:
				return render_to_response('register.html', {'form':form }, context_instance=RequestContext(request))

		args = {}
		args.update(csrf(request))

		args['form'] = UserCreationForm()
		return render_to_response('register.html', args)


def register_success(request):
	return render_to_response('register_success.html')

@login_required
def createtask(request):
	task = request.POST.get('task', '')
	status = request.POST.get('status', '')
	request.user.todolist_set.create(task=task, status=status)
	return HttpResponseRedirect('/accounts/loggedin/')

@login_required
def delete(request, pk):
	task = request.user.todolist_set.get(id = pk)
	task.delete()
	return HttpResponseRedirect('/accounts/loggedin/')

@login_required
def complete(request, pk):
	task = request.user.todolist_set.get(id = pk)
	task.status = "Complete"
	task.save()
	return HttpResponseRedirect('/accounts/loggedin/')
