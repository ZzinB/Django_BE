# Generated by Django 4.2.1 on 2023-05-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FileUpload",
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
                ("imgfile", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
    ]
