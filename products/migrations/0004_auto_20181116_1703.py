# Generated by Django 2.0.6 on 2018-11-16 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_artist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kunstenaar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='products.Artist'),
        ),
    ]
