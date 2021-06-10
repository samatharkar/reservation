# Generated by Django 3.0.6 on 2021-06-10 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0005_booking_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added on date-time'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.DateTimeField(verbose_name='End date-time'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='permanent',
            field=models.BooleanField(default=False, verbose_name='Permanently booked'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start',
            field=models.DateTimeField(verbose_name='Start date-time'),
        ),
        migrations.AlterField(
            model_name='device',
            name='added_date',
            field=models.DateField(verbose_name='Added date'),
        ),
        migrations.AlterField(
            model_name='device',
            name='arrival_date',
            field=models.DateField(verbose_name='Arrival date'),
        ),
        migrations.AlterField(
            model_name='device',
            name='bonded',
            field=models.BooleanField(default=False, verbose_name='Bonded'),
        ),
        migrations.AlterField(
            model_name='device',
            name='po_date',
            field=models.DateField(verbose_name='PO Date'),
        ),
        migrations.AlterField(
            model_name='device',
            name='shipped_date',
            field=models.DateField(verbose_name='Shipped date'),
        ),
    ]