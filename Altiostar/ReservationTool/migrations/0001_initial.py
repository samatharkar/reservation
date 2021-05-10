# Generated by Django 3.1.7 on 2021-04-30 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerType',
            fields=[
                ('server_type_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('server_type_name', models.CharField(default='NA', max_length=125)),
                ('server_make', models.CharField(default='NA', max_length=125)),
                ('server_model', models.CharField(default='NA', max_length=125)),
                ('server_processor', models.CharField(default='NA', max_length=125)),
                ('server_socket', models.CharField(default='NA', max_length=125)),
                ('server_core', models.CharField(default='NA', max_length=125)),
                ('server_hdd_model', models.CharField(default='NA', max_length=125)),
                ('server_hdd_size', models.CharField(default='NA', max_length=125)),
                ('server_hdd_number', models.CharField(default='NA', max_length=125)),
                ('server_ram', models.CharField(default='NA', max_length=125)),
            ],
            options={
                'db_table': 'server_type',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('server_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('server_name', models.CharField(default='NA', max_length=125)),
                ('server_serial_number', models.CharField(default='NA', max_length=125)),
                ('server_po_number', models.CharField(default='NA', max_length=125)),
                ('server_po_date', models.CharField(default='NA', max_length=125)),
                ('server_vendor', models.CharField(default='NA', max_length=125)),
                ('server_invoice', models.CharField(default='NA', max_length=125)),
                ('server_hdd_number', models.CharField(default='NA', max_length=125)),
                ('server_bond', models.CharField(default='NA', max_length=125)),
                ('server_bond_number', models.CharField(default='NA', max_length=125)),
                ('server_type', models.CharField(default='NA', max_length=125)),
                ('server_ship_date', models.CharField(default='NA', max_length=125)),
                ('server_arrival_date', models.CharField(default='NA', max_length=125)),
                ('server_warranty', models.CharField(default='NA', max_length=125)),
                ('server_added_byuser', models.CharField(default='NA', max_length=125)),
                ('server_added_ondate', models.CharField(default='NA', max_length=125)),
                ('server_ownership', models.CharField(default='NA', max_length=125)),
                ('server_ip_address', models.CharField(default='NA', max_length=125)),
                ('server_hostname', models.CharField(default='NA', max_length=125)),
                ('server_mgmt_mac', models.CharField(default='NA', max_length=125)),
                ('server_lan_mac', models.CharField(default='NA', max_length=125)),
                ('server_os', models.CharField(default='NA', max_length=125)),
                ('server_fversion', models.CharField(default='NA', max_length=125)),
                ('server_hardware_revision', models.CharField(default='NA', max_length=125)),
                ('server_setup_id', models.CharField(default='NA', max_length=125)),
                ('server_remark', models.CharField(default='NA', max_length=125)),
                ('server_type_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ReservationTool.servertype')),
            ],
            options={
                'db_table': 'add_server',
            },
        ),
    ]
