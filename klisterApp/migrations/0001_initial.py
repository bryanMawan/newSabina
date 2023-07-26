# Generated by Django 4.2.3 on 2023-07-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="formPage",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                (
                    "stadsdel",
                    models.CharField(
                        choices=[
                            ("Stadsområde Centrum", "Stadsområde Centrum"),
                            ("Stadsområde Nordost", "Stadsområde Nordost"),
                            ("Stadsområde Sydväst", "Stadsområde Sydväst"),
                            ("Stadsområde Hisingen", "Stadsområde Hisingen"),
                        ],
                        max_length=21,
                    ),
                ),
                ("idrott", models.CharField(max_length=100)),
                (
                    "önskad_idrott",
                    models.CharField(max_length=100, verbose_name="Önskad idrott"),
                ),
                ("in_a_union", models.BooleanField()),
                ("filePath", models.CharField(max_length=200)),
            ],
        ),
    ]
