# Generated by Django 4.2.3 on 2023-07-31 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("klisterApp", "0006_rename_id_spreadsheetid_idstring"),
    ]

    operations = [
        migrations.DeleteModel(name="SpreadsheetId",),
    ]
