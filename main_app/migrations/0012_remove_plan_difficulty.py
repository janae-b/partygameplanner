# Generated by Django 3.2.2 on 2021-05-11 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_plan_emoji'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='difficulty',
        ),
    ]
