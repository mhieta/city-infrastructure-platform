# Generated by Django 2.2.12 on 2020-05-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0016_remove_old_mount_type_fields"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mountplan", old_name="type", new_name="mount_type",
        ),
        migrations.RenameField(
            model_name="mountreal", old_name="type", new_name="mount_type",
        ),
        migrations.AddField(
            model_name="mountplan",
            name="base",
            field=models.CharField(blank=True, max_length=128, verbose_name="Base"),
        ),
        migrations.AddField(
            model_name="mountreal",
            name="base",
            field=models.CharField(blank=True, max_length=128, verbose_name="Base"),
        ),
    ]