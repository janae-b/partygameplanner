# Generated by Django 3.2.2 on 2021-05-10 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_photo_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='plan',
        ),
    ]