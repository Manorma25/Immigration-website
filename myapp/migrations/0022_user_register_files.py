# Generated by Django 4.2.2 on 2023-07-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0021_eligible"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_register",
            name="files",
            field=models.FileField(default=1, upload_to=""),
            preserve_default=False,
        ),
    ]
