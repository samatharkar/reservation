# Generated by Django 3.1.7 on 2021-05-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0017_auto_20210511_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(default='NA', max_length=125),
        ),
    ]
