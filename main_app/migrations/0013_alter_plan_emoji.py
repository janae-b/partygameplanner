# Generated by Django 3.2.2 on 2021-05-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_plan_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='emoji',
            field=models.CharField(choices=[('A', '๐ฌ'), ('Y', '๐งถ'), ('M', '๐งต'), ('H', '๐ฉ'), ('C', '๐๏ธ'), ('R', '๐'), ('P', '\U0001fa85'), ('B', '๐'), ('T', '๐'), ('S', '๐คฉ'), ('1', '๐พ'), ('2', '๐'), ('3', '\U0001f978')], default='A', max_length=1),
        ),
    ]
