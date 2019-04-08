from django.forms import ModelForm
from chat.models import *

class Index_Form(ModelForm):
    class Meta:
        model = Chat
        fields = ['chat_name']

class Room_Form(ModelForm):
    class Meta:
        model = Chat_cont
        fields = ['chat_cont']
