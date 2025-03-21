# Generated by Django 5.0.4 on 2024-04-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bio",
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
                ("bio_text", models.CharField(max_length=200)),
                ("edit_date", models.DateTimeField(verbose_name="date edited")),
            ],
        ),
    ]
