# Generated by Django 4.2.2 on 2023-07-04 10:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_blogs_coaching"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="country",
            name="id",
        ),
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name="con_details",
            fields=[
                ("image", models.ImageField(blank=True, upload_to="data")),
                (
                    "headings",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("des", ckeditor.fields.RichTextField()),
                (
                    "country_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.country"
                    ),
                ),
            ],
        ),
    ]
