# Generated by Django 5.0.4 on 2024-04-20 06:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100)),
                ('city_town', models.CharField(max_length=50)),
                ('postcode_zip', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pics')),
                ('nid_number', models.CharField(blank=True, max_length=20)),
                ('additional_information', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
