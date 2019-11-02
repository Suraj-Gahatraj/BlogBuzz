from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


class Post(mode.Model):
    author=models.ForeignKey('auth.User')
    title models.CharField(max_length=200)
    text=models.TextField()
    create_data=models.DateTimeField(default=timezone.now())