# Generated by Django 5.1.4 on 2025-01-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_alter_pizzamodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzamodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
