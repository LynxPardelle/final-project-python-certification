from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, null=True, blank=True)
    web_page = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
