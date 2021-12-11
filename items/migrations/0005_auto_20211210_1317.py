# Generated by Django 3.1.4 on 2021-12-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20211209_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Vehicles', 'Vehicles'), ('Coins & Bullion', 'Coins & Bullion'), ('Art', 'Art')], default='Vehicles', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='item_img/'),
        ),
    ]
