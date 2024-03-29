# Generated by Django 3.2.7 on 2021-11-13 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211101_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='num_packages',
            field=models.IntegerField(verbose_name='Number of packages received'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='consumers/img/profile_img/', verbose_name='Profile Picture'),
        ),
    ]
