# Generated by Django 3.2.2 on 2021-05-08 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210508_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='credit',
            field=models.URLField(default='null'),
            preserve_default=False,
        ),
    ]