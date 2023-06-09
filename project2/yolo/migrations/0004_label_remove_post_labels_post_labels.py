# Generated by Django 4.2.1 on 2023-06-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("yolo", "0003_alter_post_labels"),
    ]

    operations = [
        migrations.CreateModel(
            name="Label",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="post",
            name="labels",
        ),
        migrations.AddField(
            model_name="post",
            name="labels",
            field=models.ManyToManyField(to="yolo.label"),
        ),
    ]
