# Generated by Django 3.2.7 on 2021-12-12 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='users/img/cover_img/', verbose_name='Cover Picture'),
        ),
    ]
