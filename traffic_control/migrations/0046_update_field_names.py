# Generated by Django 2.2.17 on 2020-12-16 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0045_update_traffic_control_device_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coverageareacategory",
            name="name",
            field=models.CharField(blank=True, max_length=200, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="groupoperationalarea",
            name="areas",
            field=models.ManyToManyField(
                blank=True,
                related_name="groups",
                to="traffic_control.OperationalArea",
                verbose_name="Operational areas",
            ),
        ),
        migrations.AlterField(
            model_name="groupoperationalarea",
            name="group",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="operational_area",
                to="auth.Group",
                verbose_name="Group",
            ),
        ),
    ]