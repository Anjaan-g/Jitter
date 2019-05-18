from django.conf import settings
from django.db.models import Q
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
User = settings.AUTH_USER_MODEL

class PostQuerySet(models.QuerySet):
    def published(self):
        now=timezone.now()
        return self.filter(publish_date__lte=now)
    def search(self, query):
        lookup = (
            Q(user__username__icontains=query)|
            Q(user__email__icontains=query)|
            Q(user__first_name__icontains=query)

            )
        return self.filter(lookup)


class PostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
    def published(self):
        return self.get_queryset().published()
    def search(self,query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class Post(models.Model):
    user = models.ForeignKey(User, default =1, null=True, on_delete=models.SET_NULL )
    image = models.ImageField(upload_to='image/',null=True, blank = True)
    post_text = models.CharField(max_length = 500)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']
