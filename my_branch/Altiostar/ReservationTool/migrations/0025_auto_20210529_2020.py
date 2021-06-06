# Generated by Django 3.0.6 on 2021-05-29 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0024_auto_20210528_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=125)),
                ('bookable', models.BooleanField(default=False)),
                ('remark', models.CharField(default='NA', max_length=125)),
            ],
            options={
                'db_table': 'setups',
            },
        ),
        migrations.DeleteModel(
            name='CreateSetup',
        ),
        migrations.AlterField(
            model_name='consumable',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='device',
            name='added_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='arrival_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='device',
            name='po_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='shipped_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='setuptype',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='setuptype',
            table='setup_types',
        ),
        migrations.AlterModelTable(
            name='team',
            table='teams',
        ),
        migrations.AlterModelTable(
            name='vendor',
            table='vendors',
        ),
        migrations.DeleteModel(
            name='MakeSetup',
        ),
        migrations.AddField(
            model_name='setup',
            name='booked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.Team'),
        ),
        migrations.AddField(
            model_name='setup',
            name='consumable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.Consumable'),
        ),
        migrations.AddField(
            model_name='setup',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.Device'),
        ),
        migrations.AddField(
            model_name='setup',
            name='setup_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.SetupType'),
        ),
        migrations.AddField(
            model_name='setup',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.DeviceType'),
        ),
    ]