# Generated by Django 3.2.7 on 2021-09-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_consumer_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='subscription_status',
            field=models.CharField(choices=[('A', 'Active'), ('P', 'Pending'), ('S', 'Suspended')], default='A', max_length=1, verbose_name='Subscription Status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consumer',
            name='profile_img',
            field=models.ImageField(upload_to='consumers/img/profile_img/', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='profile_img',
            field=models.ImageField(upload_to='provider/img/profile_img/', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profile_img',
            field=models.ImageField(upload_to='users/img/profile_img/', verbose_name='Profile Picture'),
        ),
    ]
