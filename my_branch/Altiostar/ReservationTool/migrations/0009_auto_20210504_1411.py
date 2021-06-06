# Generated by Django 3.1.7 on 2021-05-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0008_auto_20210504_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateSetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_setup_name', models.CharField(max_length=125, null=True)),
                ('create_setup_remark', models.CharField(max_length=125)),
            ],
            options={
                'db_table': 'create_setups',
            },
        ),
        migrations.DeleteModel(
            name='Setup',
        ),
    ]