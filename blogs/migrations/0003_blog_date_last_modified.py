# Generated by Django 5.2.4 on 2025-07-04 20:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_blog_date_added"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="date_last_modified",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
