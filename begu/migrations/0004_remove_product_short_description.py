# Generated by Django 5.0.1 on 2024-02-22 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('begu', '0003_product_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='short_description',
        ),
    ]