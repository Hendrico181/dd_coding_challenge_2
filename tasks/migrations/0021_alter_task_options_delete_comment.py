# Generated by Django 4.1.7 on 2023-03-27 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_remove_task_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['header']},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
