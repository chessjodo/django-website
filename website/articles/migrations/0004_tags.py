# Generated by Django 5.0.4 on 2024-04-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tags",
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
                ("text", models.CharField(max_length=50)),
                ("count", models.IntegerField(default=0)),
            ],
        ),
    ]
