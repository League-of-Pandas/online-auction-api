# Generated by Django 3.1.4 on 2021-12-12 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_remove_item_min_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='bidder',
        ),
    ]