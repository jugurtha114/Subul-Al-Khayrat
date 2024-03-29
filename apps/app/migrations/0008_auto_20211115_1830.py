# Generated by Django 3.2.7 on 2021-11-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211115_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='state',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='zip',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='state',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='zip',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='state',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='zip',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Zip Code'),
        ),
    ]
