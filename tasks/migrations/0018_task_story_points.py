# Generated by Django 4.1.7 on 2023-03-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_remove_task_status_remove_task_story_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='story_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
