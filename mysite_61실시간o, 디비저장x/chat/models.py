from django.db import models

# Create your models here.
class Chat(models.Model):
    chat_name = models.CharField(max_length=50)
    
class Chat_cont(models.Model):
    #chat = models.ForeignKey(Chat, )
    chat_cont = models.CharField(max_length=50)