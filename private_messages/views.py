import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from private_messages.forms import SendMessageForm
from private_messages.models import *


def delete_messages(request, id):
    PrivateMessages.objects.filter(id=id, recipient=request.user).delete()

    return HttpResponseRedirect('/messages/')


def show_messages(request, id):
    n = PrivateMessages.objects.get(id=id)
    n.viewed = True
    n.save()

    return render(request, 'message.html', {'notification': n})


def messages(request):
    m = PrivateMessages.objects.filter(recipient=request.user).order_by('-published')

    return render(request, 'messages.html', {'messages': m})

@csrf_protect
def send_message(request):
    args = {}
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