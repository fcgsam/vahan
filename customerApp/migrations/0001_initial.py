# Generated by Django 4.2.14 on 2024-08-01 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendorApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('pickup_at', models.TimeField()),
                ('ride_status', models.CharField(choices=[('cancelled', 'cancelled'), ('Started', 'Started'), ('completed', 'completed')], max_length=20)),
                ('Front_pic', models.ImageField(default=None, upload_to='ride_images')),
                ('Back_pic', models.ImageField(default=None, upload_to='ride_images')),
                ('selfie', models.ImageField(default=None, upload_to='ride_images')),
                ('opening_kms_screen', models.ImageField(default=None, upload_to='ride_images')),
                ('closing_kms_screen', models.ImageField(default=None, upload_to='ride_images')),
                ('costomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorApp.driver')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorApp.route')),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kms', models.IntegerField()),
                ('duration', models.DurationField()),
                ('toll_fare', models.IntegerField()),
                ('parking_fare', models.IntegerField()),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerApp.ride')),
            ],
        ),
    ]
