# Generated by Django 2.0 on 2018-01-30 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('karbar', '0003_auto_20180130_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hamyar',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='karbar.MyUser')),
                ('report_method', models.IntegerField(choices=[(1, 'email'), (0, 'text')])),
            ],
            bases=('karbar.myuser',),
        ),
    ]
