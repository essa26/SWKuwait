from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from main.models import Log


def getLogs(request):
    context = {}
    user = request.user
    logs = Log.objects.filter(user=user)
    context['logs'] = logs
    template = 'index.html'

    return render_to_response(template, context, context_instance=RequestContext(request))

#def bloodTest(request):

