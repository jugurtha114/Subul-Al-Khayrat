# Generated by Django 3.2.7 on 2021-12-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211208_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='num_packages',
            field=models.IntegerField(default=1, verbose_name='Number of packages received'),
        ),
    ]
