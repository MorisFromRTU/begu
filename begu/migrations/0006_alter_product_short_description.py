# Generated by Django 5.0.1 on 2024-02-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('begu', '0005_product_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(max_length=40),
        ),
    ]