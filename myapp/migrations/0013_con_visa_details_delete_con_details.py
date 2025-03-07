# Generated by Django 4.2.2 on 2023-07-04 10:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0012_con_details_visa_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="con_visa_details",
            fields=[
                ("image1", models.ImageField(blank=True, upload_to="data")),
                ("image2", models.ImageField(blank=True, upload_to="data")),
                (
                    "headings",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("con_visa_des", ckeditor.fields.RichTextField()),
                (
                    "country_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.country"
                    ),
                ),
                (
                    "visa_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.visa_type",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="con_details",
        ),
    ]
