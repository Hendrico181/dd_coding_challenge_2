# Generated by Django 4.1.7 on 2023-03-25 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='tasks.taskstatus'),
        ),
    ]
