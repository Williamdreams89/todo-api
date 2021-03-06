# Generated by Django 4.0.5 on 2022-06-29 23:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapi', '0002_alter_todo_options_alter_todo_begins_alter_todo_ends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='begins',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todo',
            name='ends',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
