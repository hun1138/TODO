# Generated by Django 2.1.3 on 2018-11-03 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo_info',
            new_name='todo_detail',
        ),
    ]
