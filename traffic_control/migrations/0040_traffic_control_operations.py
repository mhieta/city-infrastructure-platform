# Generated by Django 2.2.16 on 2020-11-17 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("traffic_control", "0039_location_2d_to_3d"),
    ]

    operations = [
        migrations.CreateModel(
            name="OperationType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="name")),
                (
                    "traffic_sign",
                    models.BooleanField(default=False, verbose_name="traffic sign"),
                ),
                (
                    "additional_sign",
                    models.BooleanField(default=False, verbose_name="additional sign"),
                ),
                (
                    "road_marking",
                    models.BooleanField(default=False, verbose_name="road marking"),
                ),
                ("barrier", models.BooleanField(default=False, verbose_name="barrier")),
                (
                    "signpost",
                    models.BooleanField(default=False, verbose_name="signpost"),
                ),
                (
                    "traffic_light",
                    models.BooleanField(default=False, verbose_name="traffic light"),
                ),
                ("mount", models.BooleanField(default=False, verbose_name="mount")),
            ],
            options={
                "verbose_name": "operation type",
                "verbose_name_plural": "operation types",
            },
        ),
        migrations.CreateModel(
            name="TrafficSignRealOperation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("operation_date", models.DateField(verbose_name="operation date")),
                (
                    "straightness_value",
                    models.FloatField(
                        blank=True, null=True, verbose_name="straightness value"
                    ),
                ),
                (
                    "quality_requirements_fulfilled",
                    models.BooleanField(
                        default=False, verbose_name="quality requirements fulfilled"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_by_trafficsignrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        limit_choices_to={"traffic_sign": True},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="traffic_control.OperationType",
                        verbose_name="operation type",
                    ),
                ),
                (
                    "traffic_sign_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="operations",
                        to="traffic_control.TrafficSignReal",
                        verbose_name="traffic sign real",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="updated_by_trafficsignrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updated by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Traffic sign real operation",
                "verbose_name_plural": "Traffic sign real operations",
                "db_table": "traffic_sign_real_operation",
                "ordering": ["operation_date"],
            },
        ),
        migrations.CreateModel(
            name="TrafficLightRealOperation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("operation_date", models.DateField(verbose_name="operation date")),
                (
                    "straightness_value",
                    models.FloatField(
                        blank=True, null=True, verbose_name="straightness value"
                    ),
                ),
                (
                    "quality_requirements_fulfilled",
                    models.BooleanField(
                        default=False, verbose_name="quality requirements fulfilled"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_by_trafficlightrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        limit_choices_to={"traffic_light": True},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="traffic_control.OperationType",
                        verbose_name="operation type",
                    ),
                ),
                (
                    "traffic_light_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="operations",
                        to="traffic_control.TrafficLightReal",
                        verbose_name="traffic light real",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="updated_by_trafficlightrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updated by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Traffic light real operation",
                "verbose_name_plural": "Traffic light real operations",
                "db_table": "traffic_light_real_operation",
                "ordering": ["operation_date"],
            },
        ),
        migrations.CreateModel(
            name="SignpostRealOperation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("operation_date", models.DateField(verbose_name="operation date")),
                (
                    "straightness_value",
                    models.FloatField(
                        blank=True, null=True, verbose_name="straightness value"
                    ),
                ),
                (
                    "quality_requirements_fulfilled",
                    models.BooleanField(
                        default=False, verbose_name="quality requirements fulfilled"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_by_signpostrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        limit_choices_to={"signpost": True},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="traffic_control.OperationType",
                        verbose_name="operation type",
                    ),
                ),
                (
                    "signpost_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="operations",
                        to="traffic_control.SignpostReal",
                        verbose_name="signpost real",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="updated_by_signpostrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updated by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Signpost real operation",
                "verbose_name_plural": "Signpost real operations",
                "db_table": "signpost_real_operation",
                "ordering": ["operation_date"],
            },
        ),
        migrations.CreateModel(
            name="RoadMarkingRealOperation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("operation_date", models.DateField(verbose_name="operation date")),
                (
                    "straightness_value",
                    models.FloatField(
                        blank=True, null=True, verbose_name="straightness value"
                    ),
                ),
                (
                    "quality_requirements_fulfilled",
                    models.BooleanField(
                        default=False, verbose_name="quality requirements fulfilled"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_by_roadmarkingrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        limit_choices_to={"road_marking": True},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="traffic_control.OperationType",
                        verbose_name="operation type",
                    ),
                ),
                (
                    "road_marking_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="operations",
                        to="traffic_control.RoadMarkingReal",
                        verbose_name="road marking real",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="updated_by_roadmarkingrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updated by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Road marking real operation",
                "verbose_name_plural": "Road marking real operations",
                "db_table": "road_marking_real_operation",
                "ordering": ["operation_date"],
            },
        ),
        migrations.CreateModel(
            name="MountRealOperation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("operation_date", models.DateField(verbose_name="operation date")),
                (
                    "straightness_value",
                    models.FloatField(
                        blank=True, null=True, verbose_name="straightness value"
                    ),
                ),
                (
                    "quality_requirements_fulfilled",
                    models.BooleanField(
                        default=False, verbose_name="quality requirements fulfilled"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_by_mountrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "mount_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="operations",
                        to="traffic_control.MountReal",
                        verbose_name="mount real",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        limit_choices_to={"mount": True},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="traffic_control.OperationType",
                        verbose_name="operation type",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="updated_by_mountrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updated by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mount real operation",
                "verbose_name_plural": "Mount real operations",
                "db_table": "mount_real_operation",
                "ordering": ["operation_date"],
            },
        ),
        migrations.CreateModel(
            name="BarrierRealOperation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("operation_date", models.DateField(verbose_name="operation date")),
                (
                    "straightness_value",
                    models.FloatField(
                        blank=True, null=True, verbose_name="straightness value"
                    ),
                ),
                (
                    "quality_requirements_fulfilled",
                    models.BooleanField(
                        default=False, verbose_name="quality requirements fulfilled"
                    ),
                ),
                (
                    "barrier_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="operations",
                        to="traffic_control.BarrierReal",
                        verbose_name="barrier real",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_by_barrierrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        limit_choices_to={"barrier": True},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="traffic_control.OperationType",
                        verbose_name="operation type",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="updated_by_barrierrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updated by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Barrier real operation",
                "verbose_name_plural": "Barrier real operations",
                "db_table": "barrier_real_operation",
                "ordering": ["operation_date"],
            },
        ),
        migrations.CreateModel(
            name="AdditionalSignRealOperation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("operation_date", models.DateField(verbose_name="operation date")),
                (
                    "straightness_value",
                    models.FloatField(
                        blank=True, null=True, verbose_name="straightness value"
                    ),
                ),
                (
                    "quality_requirements_fulfilled",
                    models.BooleanField(
                        default=False, verbose_name="quality requirements fulfilled"
                    ),
                ),
                (
                    "additional_sign_real",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="operations",
                        to="traffic_control.AdditionalSignReal",
                        verbose_name="additional sign real",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_by_additionalsignrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "operation_type",
                    models.ForeignKey(
                        limit_choices_to={"additional_sign": True},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="traffic_control.OperationType",
                        verbose_name="operation type",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="updated_by_additionalsignrealoperation_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updated by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Additional sign real operation",
                "verbose_name_plural": "Additional sign real operations",
                "db_table": "additional_sign_real_operation",
                "ordering": ["operation_date"],
            },
        ),
    ]