# Generated by Django 5.1.2 on 2024-10-21 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fiesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salon', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('antiguedad', models.DateTimeField()),
                ('capacidad', models.IntegerField()),
            ],
        ),
    ]