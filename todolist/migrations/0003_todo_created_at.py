# Generated by Django 3.2.6 on 2021-08-09 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20210809_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
