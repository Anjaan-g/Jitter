import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# class Posts(models.Model):
#     post_text = models.CharField(max_length = 500)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.post_text
#     def was_published_recently(self):
#         # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
