# Generated by Django 5.0.6 on 2024-11-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Url",
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
                ("long_url", models.URLField(max_length=400)),
                ("short_url", models.CharField(max_length=6, unique=True)),
                ("clicks", models.IntegerField(default=0)),
            ],
        ),
    ]
