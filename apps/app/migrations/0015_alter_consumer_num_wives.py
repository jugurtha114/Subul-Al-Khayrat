# Generated by Django 3.2.7 on 2021-12-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_consumer_num_wives'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='num_wives',
            field=models.IntegerField(default=0, verbose_name='Number of wives'),
        ),
    ]
