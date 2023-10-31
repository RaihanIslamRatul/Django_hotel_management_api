# Generated by Django 4.2.6 on 2023-10-31 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0002_hotel_facilities_hotel_services_hotelroom_furniture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelroom',
            name='size',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')]),
        ),
    ]