# Generated by Django 2.2 on 2019-05-19 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]