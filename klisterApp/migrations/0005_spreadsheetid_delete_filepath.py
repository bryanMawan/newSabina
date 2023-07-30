# Generated by Django 4.2.3 on 2023-07-30 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("klisterApp", "0004_rename_password_filepath_path"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpreadsheetId",
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
                ("ID", models.CharField(max_length=1024)),
            ],
        ),
        migrations.DeleteModel(name="FilePath",),
    ]
