# Generated by Django 3.2.2 on 2021-05-12 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_plan_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='emoji',
            field=models.CharField(choices=[('A', '🍬'), ('Y', '🧶'), ('M', '🧵'), ('H', '🎩'), ('P', '🥳'), ('R', '🙌'), ('P', '\U0001fa85'), ('B', '🎂'), ('T', '🎊'), ('S', '🤩'), ('1', '👾'), ('2', '😎'), ('3', '\U0001f978'), ('4', '🎈')], default='A', max_length=1),
        ),
    ]