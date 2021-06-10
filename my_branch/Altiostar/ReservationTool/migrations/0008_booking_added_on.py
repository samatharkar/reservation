# Generated by Django 3.0.6 on 2021-06-10 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0007_auto_20210610_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Added on date-time'),
            preserve_default=False,
        ),
    ]