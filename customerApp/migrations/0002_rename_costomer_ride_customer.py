# Generated by Django 4.2.14 on 2024-08-01 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='costomer',
            new_name='customer',
        ),
    ]
