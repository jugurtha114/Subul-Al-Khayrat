# Generated by Django 3.2.7 on 2021-12-08 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=None, max_length=12, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.SlugField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=40, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=40, null=True, verbose_name='State')),
                ('zip', models.CharField(blank=True, max_length=30, null=True, verbose_name='Zip Code')),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='users/img/profile_img/', verbose_name='Profile Picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
