# Generated by Django 4.1.4 on 2023-01-02 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sub", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sub_log",
            name="id_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
