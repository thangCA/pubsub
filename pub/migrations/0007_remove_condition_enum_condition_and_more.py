# Generated by Django 4.1.4 on 2023-01-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pub", "0006_log_change_condittion"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="condition_enum",
            name="condition",
        ),
        migrations.RemoveField(
            model_name="log_change_condittion",
            name="condition",
        ),
        migrations.RemoveField(
            model_name="log_change_condittion",
            name="log_id",
        ),
        migrations.DeleteModel(
            name="Condition",
        ),
        migrations.DeleteModel(
            name="Condition_enum",
        ),
        migrations.DeleteModel(
            name="log_change_condittion",
        ),
    ]
