# Generated by Django 3.0.8 on 2020-08-05 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('hotels', '0002_auto_20200805_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.DecimalField(decimal_places=1, max_digits=2)),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.Review')),
            ],
            options={
                'db_table': 'media',
            },
        ),
    ]
