# Generated by Django 5.1.2 on 2024-11-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_rename_construido_fiesta_construido'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiesta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_fiestas/'),
        ),
    ]