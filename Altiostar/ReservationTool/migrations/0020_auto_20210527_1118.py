# Generated by Django 3.1.7 on 2021-05-27 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationTool', '0019_auto_20210524_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='makesetup',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.devicetype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='makesetup',
            name='consumable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.consumable'),
        ),
        migrations.AlterField(
            model_name='makesetup',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='make_setup', to='ReservationTool.device'),
        ),
    ]
