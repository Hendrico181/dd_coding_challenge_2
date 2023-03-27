from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import Lower
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    header = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    story_points = models.IntegerField(null=True, blank=True, default=0)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['complete']

    def __str__(self):
        return self.header
