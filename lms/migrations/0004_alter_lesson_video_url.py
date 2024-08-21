# Generated by Django 4.2 on 2024-08-21 00:12

from django.db import migrations, models
import lms.validators


class Migration(migrations.Migration):
    dependencies = [
        ("lms", "0003_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="video_url",
            field=models.URLField(validators=[lms.validators.validate_youtube_url]),
        ),
    ]
