# Generated by Django 2.2.14 on 2020-07-29 11:25

from django.db import migrations


def bypass_operational_area_for_existing_users(apps, schema_editor):
    User = apps.get_model("users", "User")
    User.objects.all().update(bypass_operational_area=True)


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_operational_area"),
    ]

    operations = [
        migrations.RunPython(
            bypass_operational_area_for_existing_users, migrations.RunPython.noop
        )
    ]