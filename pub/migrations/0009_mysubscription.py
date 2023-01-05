# Generated by Django 4.1.4 on 2023-01-05 02:31

from django.db import migrations, models
import model_subscription.mixin


class Migration(migrations.Migration):

    dependencies = [
        ("pub", "0008_condition_log_change_condittion_condition_enum"),
    ]

    operations = [
        migrations.CreateModel(
            name="MySubscription",
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
            ],
            options={
                "abstract": False,
            },
            bases=(model_subscription.mixin.SubscriptionModelMixin, models.Model),
        ),
    ]
