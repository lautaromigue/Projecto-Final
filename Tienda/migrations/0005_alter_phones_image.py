# Generated by Django 4.0.6 on 2022-09-06 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0004_consoles_image_peripherals_image_phones_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='phone_images/'),
        ),
    ]
