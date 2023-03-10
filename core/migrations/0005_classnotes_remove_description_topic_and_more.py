# Generated by Django 4.1.6 on 2023-02-16 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_imageupload_date_added"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClassNotes",
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
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="uploads")),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.classname"
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="description", name="topic",),
        migrations.DeleteModel(name="ImageUpload",),
        migrations.DeleteModel(name="Description",),
    ]
