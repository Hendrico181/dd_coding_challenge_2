# Generated by Django 4.1.7 on 2023-03-25 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_alter_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.DeleteModel(
            name='TaskStatus',
        ),
    ]
