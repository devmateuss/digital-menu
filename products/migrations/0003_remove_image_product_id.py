# Generated by Django 4.0.5 on 2022-06-26 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='product_id',
        ),
    ]
