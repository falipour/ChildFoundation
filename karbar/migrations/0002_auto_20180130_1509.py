# Generated by Django 2.0 on 2018-01-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karbar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='national_id',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]