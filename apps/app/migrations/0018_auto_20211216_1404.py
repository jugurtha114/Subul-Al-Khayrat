# Generated by Django 3.2.7 on 2021-12-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_consumer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
