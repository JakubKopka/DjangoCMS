import datetime

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from pytz import unicode

from DjangoCMS.forms import RegisterForm


@csrf_protect
def login(request):
    c = {}
    c.update(csrf(request))
    c['title'] = "Logowanie"
    return render_to_response('login.html', c)

@csrf_protect
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        c = {'error': "Błąd logowania!"}
        c.update(csrf(request))
        return render(request, 'login.html', c)


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def loggedin(request):
    return render_to_response('loggedin.html', {'user_name': request.user.username})


def invalid(request):
    return render(request, 'error.html', {'error': "Błąd logowania!"})

@csrf_protect
def register(request):
    args = {}
    args['title'] = "Rejestracja"
    args.update(csrf(request))
    form = RegisterForm()

    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    args['form'] = form
    print(form.errors.values())
    return render(request, 'register.html', args)


def register_success(request):
    return render_to_response('register_success.html')


def ajax(request):
    d = datetime.datetime.now()
    return HttpResponse(d.strftime("%d-%m-%Y %H:%M:%S"))
