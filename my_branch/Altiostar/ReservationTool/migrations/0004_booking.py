# Generated by Django 3.0.6 on 2021-06-10 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReservationTool', '0003_auto_20210610_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('permanent', models.BooleanField(default=False)),
                ('setup', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='Booking', to='ReservationTool.Setup')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='Booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
