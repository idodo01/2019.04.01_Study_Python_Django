from django.shortcuts import render
from django.utils.safestring import mark_safe
from chat.forms import *
import json

def index(request):
    if request.method == 'POST':
        index_form = Index_Form(request.POST)
        if index_form.is_valid():
            index_form.save()
    else:
        index_form = Index_Form()

    return render(request, 'chat/index.html', {'index_form':index_form})

def room(request, room_name):

    chat_cont_all = Chat_cont.objects.all()

    if request.method == 'POST':
        room_form = Room_Form(request.POST)
        if room_form.is_valid():
            room_form.save()
    else:
        room_form = Room_Form()

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'room_form':room_form,
        'chat_cont_all':chat_cont_all

    })

