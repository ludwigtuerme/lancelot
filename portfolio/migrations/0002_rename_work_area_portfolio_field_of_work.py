# Generated by Django 5.0.2 on 2024-03-04 00:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="portfolio",
            old_name="work_area",
            new_name="field_of_work",
        ),
    ]
