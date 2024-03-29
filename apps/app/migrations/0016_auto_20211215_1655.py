# Generated by Django 3.2.7 on 2021-12-15 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_consumer_num_wives'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='gender',
            field=models.SlugField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.package'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='gender',
            field=models.SlugField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
