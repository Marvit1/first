# Generated by Django 5.1 on 2024-08-15 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0012_reclam"),
    ]

    operations = [
        migrations.AddField(
            model_name="reclam",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reclam",
                to="main.category",
            ),
        ),
    ]
