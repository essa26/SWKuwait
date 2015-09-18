from datetime import datetime
from django.shortcuts import render_to_response

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


def bloodTest(request):
    context = {}
    if request.method == 'GET':
        template = 'test.html' # means, go to the blood test page
        return render_to_response(template, context, context_instance=RequestContext(request))
    else:
        bloodsugar = int(request.POST.get('bloodsugar'))
        print bloodsugar+5
        # do calculations here
        if bloodsugar <= 97 and bloodsugar > 0:
            # very low
            msg = "Very Low"

        elif bloodsugar > 97 and bloodsugar <= 133:
            # low
            msg = "Low"

        elif bloodsugar > 133 and bloodsugar <= 168:
            # normal
            msg = "Normal"

        elif bloodsugar > 168 and bloodsugar <= 240:
            # high
            msg = "High"

        elif bloodsugar > 240:
            # very high
            msg = "Very High"
        else:
            msg = "The laws of mathematics do not allow this error to logically exist"


        if request.user.is_authenticated():
            # save log in database of blood test
            user = request.user
            date = datetime.datetime.now()
            log = Log.objects.create(user=user, bloodsugar=bloodsugar, date=date)
            log.save()

        context['msg'] = msg
        template = 'test.html'
        return render_to_response(template, context, context_instance=RequestContext(request))


def bloodTestResult(request):
    bloodsugar = request.GET.get('bloodsugar')
    context = {}
    # do calculations here
    if bloodsugar <= 97 and bloodsugar > 0:
        # very low
        msg = "Very Low"

    elif bloodsugar > 97 and bloodsugar <= 133:
        # low
        msg = "Low"

    elif bloodsugar > 133 and bloodsugar <= 168:
        # normal
        msg = "Normal"

    elif bloodsugar > 168 and bloodsugar <= 240:
        # high
        msg = "High"

    elif bloodsugar > 240:
        # very high
        msg = "Very High"


    if request.user.is_authenticated():
        # save log in database of blood test
        user = request.user
        date = datetime.datetime.now()
        log = Log.objects.create(user=user, bloodsugar=bloodsugar, date=date)
        log.save()

    context['msg'] = msg
    template = 'bloodtest.html'
    return render_to_response(template, context, context_instance=RequestContext(request))

