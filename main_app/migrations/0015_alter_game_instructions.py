# Generated by Django 3.2.2 on 2021-05-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_plan_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='instructions',
            field=models.TextField(default='1.\n2.\n3.\n4. ', help_text='Enter your instructions', max_length=250),
        ),
    ]
