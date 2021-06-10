# Generated by Django 3.0.6 on 2021-06-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setuptype',
            name='name',
        ),
        migrations.AddField(
            model_name='setuptype',
            name='setup_type',
            field=models.CharField(default='NA', max_length=125, verbose_name='Setup Type'),
        ),
    ]
