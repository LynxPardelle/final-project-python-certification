from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=140)
    sub_title = models.CharField(max_length=140)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='blog', null=True, blank=True)

    def __str__(self):
        return self.title
