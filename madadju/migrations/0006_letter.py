# Generated by Django 2.0 on 2018-01-30 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hamyar', '0005_auto_20180130_1616'),
        ('madadju', '0005_urgentneed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('madadju', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadju.Madadju')),
                ('receiver_hamyar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hamyar.Hamyar')),
            ],
        ),
    ]