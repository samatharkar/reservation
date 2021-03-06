# Generated by Django 3.1.7 on 2021-04-24 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('is_acquired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SetupType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
            ],
        ),
        migrations.AlterField(
            model_name='setup',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ReservationTool.device'),
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ReservationTool.devicetype'),
        ),
        migrations.AlterField(
            model_name='setup',
            name='setup_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ReservationTool.setuptype'),
        ),
    ]
