# Generated by Django 2.0 on 2018-01-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamyar', '0008_auto_20180130_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamyar',
            name='report_method',
            field=models.IntegerField(choices=[(0, 'text'), (1, 'email')]),
        ),
    ]
