# Generated by Django 3.1.4 on 2021-12-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='highest_bidder',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
