import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from private_messages.forms import SendMessageForm
from private_messages.models import *

from django.contrib.auth.decorators import login_required


@login_required
def delete_messages(request, id):
    PrivateMessages.objects.filter(id=id, recipient=request.user).delete()

    return HttpResponseRedirect('/messages/')


@login_required
def show_messages(request, id):
    n = PrivateMessages.objects.get(id=id, recipient=request.user)
    n.viewed = True
    n.save()

    return render(request, 'message.html', {'notification': n})


@login_required
def messages(request):
    data = {}
    data['title'] = "Wiadomości"
    m = PrivateMessages.objects.filter(recipient=request.user).order_by('-published')
    data['messages'] = m
    return render(request, 'messages.html', data)


@login_required
def send_message(request):
    args = {}
    args['title'] = "Wyślij wiadomość"
    args.update(csrf(request))
    form = SendMessageForm()

    if request.POST:
        recipient = User.objects.get(id=request.POST.get('recipient'))
        data = request.POST.copy()
        data['published'] = datetime.datetime.now()
        data['sender'] = request.user.id
        data['recipient'] = recipient.id
        form = SendMessageForm(data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/messages/')

    args['form'] = form
    return render(request, 'send_message.html', args)
