# Generated by Django 2.2.16 on 2020-12-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0043_unify_field_verbose_name_cases"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signpostplan",
            name="value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Signpost value",
            ),
        ),
        migrations.AlterField(
            model_name="signpostreal",
            name="value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Signpost value",
            ),
        ),
        migrations.AlterField(
            model_name="trafficsignplan",
            name="value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Traffic Sign Code value",
            ),
        ),
        migrations.AlterField(
            model_name="trafficsignreal",
            name="value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Traffic Sign Code value",
            ),
        ),
    ]