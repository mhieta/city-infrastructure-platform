# Generated by Django 2.2.12 on 2020-05-08 12:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0009_add_is_active_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="TrafficSignRealFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="realfiles/traffic_sign/", verbose_name="File"
                    ),
                ),
                (
                    "traffic_sign_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="traffic_control.TrafficSignReal",
                    ),
                ),
            ],
            options={
                "verbose_name": "Traffic Sign Real File",
                "verbose_name_plural": "Traffic Sign Real Files",
                "db_table": "traffic_sign_real_file",
            },
        ),
        migrations.CreateModel(
            name="TrafficLightRealFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="realfiles/traffic_light/", verbose_name="File"
                    ),
                ),
                (
                    "traffic_light_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="traffic_control.TrafficLightReal",
                    ),
                ),
            ],
            options={
                "verbose_name": "Traffic Light Real File",
                "verbose_name_plural": "Traffic Light Real Files",
                "db_table": "traffic_light_real_file",
            },
        ),
        migrations.CreateModel(
            name="SignpostRealFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="realfiles/signpost/", verbose_name="File"
                    ),
                ),
                (
                    "signpost_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="traffic_control.SignpostReal",
                    ),
                ),
            ],
            options={
                "verbose_name": "Signpost Real File",
                "verbose_name_plural": "Signpost Real Files",
                "db_table": "signpost_real_file",
            },
        ),
        migrations.CreateModel(
            name="RoadMarkingRealFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="realfiles/road_marking/", verbose_name="File"
                    ),
                ),
                (
                    "road_marking_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="traffic_control.RoadMarkingReal",
                    ),
                ),
            ],
            options={
                "verbose_name": "RoadMarking Real File",
                "verbose_name_plural": "RoadMarking Real Files",
                "db_table": "road_marking_real_file",
            },
        ),
        migrations.CreateModel(
            name="MountRealFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "file",
                    models.FileField(upload_to="realfiles/mount/", verbose_name="File"),
                ),
                (
                    "mount_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="traffic_control.MountReal",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mount Real File",
                "verbose_name_plural": "Mount Real Files",
                "db_table": "mount_real_file",
            },
        ),
        migrations.CreateModel(
            name="BarrierRealFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="realfiles/barrier/", verbose_name="File"
                    ),
                ),
                (
                    "barrier_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="traffic_control.BarrierReal",
                    ),
                ),
            ],
            options={
                "verbose_name": "Barrier Real File",
                "verbose_name_plural": "Barrier Real Files",
                "db_table": "barrier_real_file",
            },
        ),
    ]
