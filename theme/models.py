
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
import math
from django.conf import settings

from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE, )


class ChatRoom(models.Model):
    title = models.CharField(max_length=50)
    member_set = models.ManyToManyField(
        'MyUser', related_name='joined_room_set', blank=True)


class ChatMessage(models.Model):
    room = models.ForeignKey(
        'ChatRoom', related_name='chat_message', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        'MyUser', related_name='chat_message', on_delete=models.PROTECT)
    posted = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=200)

from django.db import models
from django.utils import timezone

# Create your models here.
class MyRoom(models.Model):
    name  = models.TextField()
    label = models.SlugField(unique=True)

class MyMessage(models.Model):
    room      = models.ForeignKey(MyRoom, related_name='messages', on_delete=models.CASCADE)
    handle    = models.TextField()
    message   = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

