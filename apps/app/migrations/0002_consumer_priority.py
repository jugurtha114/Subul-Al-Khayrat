# Generated by Django 3.2.7 on 2021-09-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='priority',
            field=models.IntegerField(default=1, verbose_name='Priority'),
        ),
    ]
