# Generated by Django 4.2.1 on 2023-05-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='task_priority',
            field=models.CharField(max_length=1),
        ),
    ]
