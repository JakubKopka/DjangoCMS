from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm


@csrf_protect
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

@csrf_protect
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        c = {'error': "Błąd logowania!"}
        c.update(csrf(request))
        return render_to_response('login.html', c)


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def loggedin(request):
    return render_to_response('loggedin.html', {'user_name': request.user.username})


def invalid(request):
    return render_to_response('error.html', {'error': "Błąd logowania!"})

@csrf_protect
def register(request):
    args = {}
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

        args['error'] = "Błąd rejestracji!"
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')
