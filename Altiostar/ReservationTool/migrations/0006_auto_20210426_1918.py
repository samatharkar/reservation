# Generated by Django 3.1.7 on 2021-04-26 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0005_auto_20210426_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetupType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Setup Name', max_length=125)),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='setup',
            name='setup_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ReservationTool.setuptype'),
        ),
    ]