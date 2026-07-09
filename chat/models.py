from django.db import models

# Create your models here.
class Chat(models.Model):
    user_message = models.TextField()
    bot_reply = models.TextField()