# Generated by Django 3.2.2 on 2021-05-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_remove_game_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(help_text='Enter the name', max_length=100),
        ),
    ]