# Generated by Django 3.1.7 on 2021-05-28 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0020_auto_20210527_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetupType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('setup_type', models.CharField(default='NA', max_length=125)),
                ('remark', models.CharField(default='NA', max_length=125)),
            ],
            options={
                'db_table': 'setup_type',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='NA', max_length=125)),
                ('manager', models.CharField(default='NA', max_length=125)),
                ('remark', models.CharField(default='NA', max_length=125)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.AddField(
            model_name='makesetup',
            name='bookable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='makesetup',
            name='remark',
            field=models.CharField(default='NA', max_length=125),
        ),
        migrations.AddField(
            model_name='makesetup',
            name='booked_by',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='makesetup',
            name='setup_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.setuptype'),
            preserve_default=False,
        ),
    ]
