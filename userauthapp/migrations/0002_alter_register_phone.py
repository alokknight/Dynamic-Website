# Generated by Django 3.2.5 on 2021-08-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.BigIntegerField(default='000'),
        ),
    ]
