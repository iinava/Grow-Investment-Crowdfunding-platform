# Generated by Django 4.2.3 on 2023-11-17 16:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fundingapp", "0005_project"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="fountation",
            new_name="foundation",
        ),
    ]