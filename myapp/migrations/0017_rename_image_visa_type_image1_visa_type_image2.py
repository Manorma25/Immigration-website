# Generated by Django 4.2.2 on 2023-07-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0016_alter_blogs_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="visa_type",
            old_name="image",
            new_name="image1",
        ),
        migrations.AddField(
            model_name="visa_type",
            name="image2",
            field=models.ImageField(blank=True, upload_to="data"),
        ),
    ]
