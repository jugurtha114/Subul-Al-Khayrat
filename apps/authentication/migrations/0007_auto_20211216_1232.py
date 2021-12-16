# Generated by Django 3.2.7 on 2021-12-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20211214_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='users/img/cover_img/', verbose_name='Cover Picture'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='users/img/profile_img/', verbose_name='Profile Picture'),
        ),
    ]
