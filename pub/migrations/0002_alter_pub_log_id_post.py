# Generated by Django 4.1.4 on 2023-01-02 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pub", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pub_log",
            name="id_post",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="pub.post"
            ),
        ),
    ]
