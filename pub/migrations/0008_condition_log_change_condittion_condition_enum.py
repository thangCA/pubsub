# Generated by Django 4.1.4 on 2023-01-03 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pub", "0007_remove_condition_enum_condition_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Condition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("condition", models.CharField(max_length=100)),
                ("field_change", models.CharField(max_length=100)),
                ("value_change", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="log_change_condittion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field_change", models.CharField(max_length=100)),
                ("before", models.JSONField(null=True)),
                ("after", models.JSONField(null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("check_change", models.BooleanField(default=True)),
                (
                    "condition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pub.condition"
                    ),
                ),
                (
                    "log_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pub.pub_log"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Condition_enum",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=100)),
                (
                    "condition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pub.condition"
                    ),
                ),
            ],
        ),
    ]
