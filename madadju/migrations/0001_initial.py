# Generated by Django 2.0 on 2018-01-30 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('karbar', '0006_auto_20180130_1537'),
        ('madadkar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Madadju',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='karbar.MyUser')),
                ('physical_state', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('grade', models.CharField(max_length=20)),
                ('account', models.IntegerField()),
                ('saving', models.IntegerField()),
                ('current_madadkar', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='madadkar.Madadkar')),
            ],
            bases=('karbar.myuser',),
        ),
    ]