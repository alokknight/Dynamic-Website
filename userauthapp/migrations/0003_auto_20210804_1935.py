# Generated by Django 3.2.5 on 2021-08-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthapp', '0002_alter_register_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(default='xyz', max_length=122),
        ),
        migrations.AlterField(
            model_name='register',
            name='firstname',
            field=models.CharField(default='xyz', max_length=122),
        ),
        migrations.AlterField(
            model_name='register',
            name='lastname',
            field=models.CharField(default='xyz', max_length=122),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(default='xyz', max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(default='xyz', max_length=122, primary_key=True, serialize=False),
        ),
    ]
