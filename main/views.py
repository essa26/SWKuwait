from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from main.forms import UserLogin
from main.models import Log


def getLogs(request):
    context = {}
    user = request.user
    logs = Log.objects.filter(user=user)
    context['logs'] = logs
    template = 'index.html'

    return render_to_response(template, context, context_instance=RequestContext(request))


def login_view(request):

    context = {}

    form = UserLogin()

    context['form'] = form

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    auth_user = authenticate(username=username, password=password)

    if auth_user is not None:
        if auth_user.is_active:
            login(request, auth_user)
            context['valid'] = "Login Successful"

            return HttpResponseRedirect('/')
        else:
            context['valid'] = form.errors

    else:
        context['valid'] = form.errors

    return render_to_response('login.html', context, context_instance=RequestContext(request))

