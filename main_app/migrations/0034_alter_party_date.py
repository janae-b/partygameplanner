# Generated by Django 3.2.2 on 2021-05-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0033_auto_20210510_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='date',
            field=models.DateField(verbose_name='Party Date'),
        ),
    ]
