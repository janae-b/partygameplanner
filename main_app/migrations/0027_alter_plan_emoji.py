# Generated by Django 3.2.2 on 2021-05-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_auto_20210513_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='emoji',
            field=models.CharField(choices=[('A', '🍬'), ('Y', '🎲'), ('M', '🔮'), ('H', '🎩'), ('E', '🥳'), ('R', '🙌'), ('P', '\U0001fa85'), ('B', '🎂'), ('T', '🎊'), ('S', '🤩'), ('1', '👾'), ('2', '😎'), ('3', '\U0001f978'), ('4', '🎈'), ('5', '🎁'), ('6', '👑'), ('7', '📝')], default='A', max_length=1),
        ),
    ]