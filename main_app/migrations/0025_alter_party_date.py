# Generated by Django 3.2.2 on 2021-05-13 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_plan_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Party Date'),
        ),
    ]
