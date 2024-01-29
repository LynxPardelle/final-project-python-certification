from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.content
