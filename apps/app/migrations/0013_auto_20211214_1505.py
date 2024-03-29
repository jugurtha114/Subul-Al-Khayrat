# Generated by Django 3.2.7 on 2021-12-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_consumer_num_packages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='num_children',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Number of Children'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='num_wives',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Number of wives'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='priority',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Priority'),
        ),
    ]
