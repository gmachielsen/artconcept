# Generated by Django 2.0.6 on 2018-11-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181117_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='lcm',
            new_name='lengthcm',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='wcm',
            new_name='widthcm',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='image5',
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
