# Generated by Django 5.0.4 on 2024-05-01 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0012_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.categorywork'),
        ),
    ]
