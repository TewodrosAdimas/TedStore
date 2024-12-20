# Generated by Django 5.0.8 on 2024-10-09 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_alter_category_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="owner",
            field=models.ForeignKey(
                default=15,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
