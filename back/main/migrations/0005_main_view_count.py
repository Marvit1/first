# Generated by Django 5.0.1 on 2024-02-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_category_options_alter_main_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="main",
            name="view_count",
            field=models.IntegerField(default=0),
        ),
    ]
