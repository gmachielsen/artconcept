# Generated by Django 2.0.6 on 2018-11-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181114_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(default=2, upload_to='artist_images'),
            preserve_default=False,
        ),
    ]
