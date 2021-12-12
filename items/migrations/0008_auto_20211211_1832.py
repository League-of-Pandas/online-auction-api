# Generated by Django 3.1.4 on 2021-12-11 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20211211_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='end_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='end_date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='start_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='start_date'),
        ),
    ]
