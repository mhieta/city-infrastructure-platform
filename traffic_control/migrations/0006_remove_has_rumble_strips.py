# Generated by Django 2.2.13 on 2020-06-29 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0005_trafficcontroldevicetype_type"),
    ]

    operations = [
        migrations.RemoveField(model_name="roadmarkingplan", name="has_rumble_strips",),
        migrations.RemoveField(model_name="roadmarkingreal", name="has_rumble_strips",),
    ]