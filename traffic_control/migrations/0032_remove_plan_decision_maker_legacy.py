# Generated by Django 2.2.16 on 2020-10-23 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0031_migrate_decision_makers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plan",
            name="decision_maker_legacy",
        ),
    ]
