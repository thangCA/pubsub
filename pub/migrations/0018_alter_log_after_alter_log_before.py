# Generated by Django 4.1.4 on 2023-01-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pub", "0017_log"),
    ]

    operations = [
        migrations.AlterField(
            model_name="log",
            name="after",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="log",
            name="before",
            field=models.JSONField(default=dict),
        ),
    ]
