# Generated by Django 5.1.6 on 2025-03-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0002_alter_category_options_alter_storegoods_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='storegoods',
            name='sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
