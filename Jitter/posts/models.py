from django.conf import settings

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user = models.ForeignKey(User, default =1, null=True, on_delete=models.SET_NULL )
    image = models.ImageField(upload_to='image/',null=True, blank = True)
    post_text = models.CharField(max_length = 500)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']
