# Generated by Django 2.2.7 on 2019-11-14 18:27

from django.db import migrations, models
import ecomapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=ecomapp.models.image_folder),
        ),
    ]
