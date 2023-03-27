from django.forms import ModelForm
from tasks.models import Task

from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from django import forms


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['header', 'description', 'user', 'story_points']
