# Generated by Django 4.1.4 on 2023-01-05 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pub", "0011_mysubscription"),
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
        migrations.RemoveField(
            model_name="pub_log",
            name="id_post",
        ),
        migrations.RemoveField(
            model_name="pub_log",
            name="id_user",
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
        migrations.DeleteModel(
            name="Pub_log",
        ),
    ]
