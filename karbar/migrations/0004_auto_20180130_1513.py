# Generated by Django 2.0 on 2018-01-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karbar', '0003_auto_20180130_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.IntegerField(choices=[(3, 'madadju'), (2, 'hamyar'), (0, 'modir'), (1, 'madadkar')]),
        ),
    ]