# Generated by Django 5.1 on 2024-08-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_main_link_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reclam",
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
                ("image", models.ImageField(blank=True, upload_to="uploads/")),
                ("thumbnail", models.ImageField(blank=True, upload_to="uploads/")),
                (
                    "published",
                    models.BooleanField(
                        default=True, verbose_name="Գրառում հրապարակված է"
                    ),
                ),
                ("link", models.URLField(blank=True)),
            ],
            options={
                "verbose_name": "Գովազդ Վերև",
                "verbose_name_plural": "Գովազդ Վերև",
            },
        ),
    ]
