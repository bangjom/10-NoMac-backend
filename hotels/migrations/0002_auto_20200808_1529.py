# Generated by Django 3.0.7 on 2020-08-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteldetail',
            name='amenity',
            field=models.ManyToManyField(through='hotels.HotelAmenity', to='hotels.Amenity'),
        ),
        migrations.AddField(
            model_name='hoteldetail',
            name='facility',
            field=models.ManyToManyField(through='hotels.HotelFacility', to='hotels.Facility'),
        ),
        migrations.AddField(
            model_name='hoteldetail',
            name='roomtype',
            field=models.ManyToManyField(through='hotels.HotelRoomtype', to='hotels.Roomtype'),
        ),
    ]
