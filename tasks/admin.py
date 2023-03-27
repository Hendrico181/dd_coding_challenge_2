from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('header', 'description', 'user', 'complete')
    exclude = ('date_created',)


admin.site.register(Task, TaskAdmin)
