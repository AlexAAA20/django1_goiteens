# Generated by Django 3.2.25 on 2024-04-11 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20240409_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
