# Generated by Django 3.2.2 on 2021-05-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_alter_game_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='instructions',
            field=models.TextField(default='1.            2.                 3.                 ', max_length=250),
        ),
    ]
