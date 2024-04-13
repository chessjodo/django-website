# Generated by Django 5.0.4 on 2024-04-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=30)),
                ("bio_text", models.CharField(max_length=200)),
                ("bio_edit", models.DateTimeField(verbose_name="info date edited")),
            ],
        ),
        migrations.DeleteModel(
            name="Bio",
        ),
    ]
