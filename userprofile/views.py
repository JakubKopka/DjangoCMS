from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from userprofile.forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):

    if request.POST:
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        user = request.user
        profile_ = user.profile
        form = ProfileForm(instance=profile_)

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render(request, "profile.html", args)
