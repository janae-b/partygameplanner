# Generated by Django 3.2.2 on 2021-05-10 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_game_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='likes',
        ),
    ]