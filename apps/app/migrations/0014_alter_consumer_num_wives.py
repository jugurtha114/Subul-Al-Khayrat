# Generated by Django 3.2.7 on 2021-12-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20211214_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='num_wives',
            field=models.SmallIntegerField(default=0, verbose_name='Number of wives'),
        ),
    ]