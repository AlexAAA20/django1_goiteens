# Generated by Django 3.2.25 on 2024-04-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='description',
            field=models.TextField(max_length=256),
        ),
    ]
