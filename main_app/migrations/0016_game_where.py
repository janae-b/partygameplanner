# Generated by Django 3.2.2 on 2021-05-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_game_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='where',
            field=models.CharField(choices=[('O', 'Outdoors'), ('I', 'Indoors'), ('B', 'Both'), ('V', 'Virtual')], default='O', max_length=1),
        ),
    ]
