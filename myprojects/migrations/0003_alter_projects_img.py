# Generated by Django 3.2.5 on 2021-08-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0002_alter_projects_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='img',
            field=models.ImageField(height_field='200', upload_to='pics', width_field='200'),
        ),
    ]
