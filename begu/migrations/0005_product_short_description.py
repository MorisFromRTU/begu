# Generated by Django 5.0.1 on 2024-02-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('begu', '0004_remove_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]