from datetime import datetime
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext
from main.forms import UserLogin, DoctorSearch, SendEmail
from main.models import Log, Clinic, DoctorProfile
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt



def getLogs(request):
    context = {}
    if request.user.is_authenticated():
        user = request.user
        userprof = user.userprofile
        logs = Log.objects.filter(user=userprof)
        context['logs'] = logs
        template = 'index.html'

        return render_to_response(template, context, context_instance=RequestContext(request))
    else:
        # user needs to be logged in to continue here
        return HttpResponseRedirect('/')


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

<<<<<<< HEAD
    return render(request, template, context)
=======
    context['msg'] = msg
    template = 'bloodtest.html'
    return render_to_response(template, context, context_instance=RequestContext(request))
>>>>>>> 72bc063bebced0b4cc1c4291d98b3385d79cd226

#login view using crispy
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

#view to list clinics

def clinic_list(request):

    context = {}

    clinics = Clinic.objects.all()

    context['clinics'] = clinics

    return render_to_response('clinic_list.html', context, context_instance=RequestContext(request))


#doctor's search view

def clinic_detail(request, pk):

    clinic = Clinic.objects.get(pk=pk)

    context = {}

    context['clinic'] = clinic

    doctors = DoctorProfile.objects.filter(clinic=clinic)

    context['doctors'] = doctors

    return render_to_response('clinic_detail.html', context, context_instance=RequestContext(request))


def doctor_search(request):

    context = {}

    get = request.GET
    post = request.POST

    context['get'] = get
    context['post'] = post

    form = DoctorSearch
    context['form'] = form

    if request.method == "POST":

        form = DoctorSearch(request.POST)
        print 1
        if form.is_valid():
            doctor = form.cleaned_data['name']
            print 2
            print doctor

            doctors = DoctorProfile.objects.filter(name__icontains=doctor)

            context['doctors'] = doctors
            context['valid'] = "The Form Was Valid"

        else:
            context['valid'] = form.errors
            print 3
    print 4
    return render_to_response('doctor_search.html', context, context_instance=RequestContext(request))


#doctor detail view

def doctor_detail_view(request, pk):

    context = {}

    doctor = DoctorProfile.objects.get(pk=pk)

    context['doctor'] = doctor

    form = SendEmail(request.POST)

    context['form'] = form

    return render_to_response('doctor_detail.html', context, context_instance=RequestContext(request))

@csrf_exempt
def send_email_view(request, pk):

    doctor = DoctorProfile.objects.get(pk=pk)

    doctor_email = doctor.email

    if request.method == 'POST':
        form = SendEmail(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = request.POST['message']

            fullemail = """%s, %s, %s:
%s""" % (name, email, phone_number, message)

            try:
                send_mail('Contact', fullemail, email, [doctor_email])

                return HttpResponseRedirect('/')
            except:
              return HttpResponseRedirect('/')
        else:
          return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

