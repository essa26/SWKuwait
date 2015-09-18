from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from main.forms import UserLogin, DoctorSearch, SendEmail
from main.models import Log, Clinic, DoctorProfile
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt



def getLogs(request):
    context = {}
    user = request.user
    logs = Log.objects.filter(user=user)
    context['logs'] = logs
    template = 'index.html'

    return render_to_response(template, context, context_instance=RequestContext(request))

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

def doctor_search(request):

    context = {}

    get = request.GET
    post = request.POST

    context['get'] = get
    context['post'] = post

    form = DoctorSearch
    context['form'] = form

    if request.method == "GET":
        form = DoctorSearch(request.GET)

        if form.is_valid():
            doctor = form.cleaned_data['name']

            print doctor

            doctors = DoctorProfile.objects.filter(tags__name__icontains=doctor)

            context['doctors'] = doctors
            context['valid'] = "The Form Was Valid"

        else:
            context['valid'] = form.errors

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

