# Generated by Django 4.2.1 on 2023-05-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='task_priority',
            field=models.CharField(default='L', max_length=1),
        ),
    ]
