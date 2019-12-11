from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    text = models.TextField(default="")
    send_time = models.DateTimeField(auto_now_add=True)
    isread = models.BooleanField(default=False)
