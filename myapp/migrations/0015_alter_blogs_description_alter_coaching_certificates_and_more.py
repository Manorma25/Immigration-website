# Generated by Django 4.2.2 on 2023-07-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0014_alter_blogs_description_alter_coaching_certificates_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="coaching",
            name="certificates",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="coaching",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="coaching",
            name="overview",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="visa_type",
            name="about",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="visa_type",
            name="doc",
            field=models.TextField(),
        ),
    ]
