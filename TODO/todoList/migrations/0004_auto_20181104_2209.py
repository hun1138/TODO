# Generated by Django 2.1.3 on 2018-11-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0003_auto_20181103_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_due_date',
            field=models.DateField(null=True),
        ),
    ]
