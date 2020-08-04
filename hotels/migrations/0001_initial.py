# Generated by Django 3.0.7 on 2020-08-07 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'amenities',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'facilities',
            },
        ),
        migrations.CreateModel(
            name='HotelDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_rating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotel_special', models.CharField(max_length=255)),
                ('hotel_special2', models.CharField(max_length=255)),
                ('english_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10)),
                ('provider_logo', models.TextField(default='', max_length=1000)),
                ('label', models.CharField(default='', max_length=255)),
                ('reservation_start_at', models.DateField(null=True)),
                ('reservation_end_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'hotel_details',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Roomtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'roomtypes',
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cleanliness', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'hotel_stars',
            },
        ),
        migrations.CreateModel(
            name='HotelRoomtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelDetail')),
                ('roomtype', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.Roomtype')),
            ],
            options={
                'db_table': 'hotel_roomtypes',
            },
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelDetail')),
                ('image', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.Image')),
            ],
            options={
                'db_table': 'hotel_images',
            },
        ),
        migrations.CreateModel(
            name='HotelFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.Facility')),
                ('hotel_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelDetail')),
            ],
            options={
                'db_table': 'hotel_facilities',
            },
        ),
        migrations.AddField(
            model_name='hoteldetail',
            name='star',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotels.Star'),
        ),
        migrations.CreateModel(
            name='HotelAmenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.Amenity')),
                ('hotel_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelDetail')),
            ],
            options={
                'db_table': 'hotel_amenities',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('flat', models.CharField(default='', max_length=255)),
                ('user_rating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Country')),
                ('hotel_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotels.HotelDetail')),
            ],
            options={
                'db_table': 'hotels',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Country'),
        ),
    ]
