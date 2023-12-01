# Generated by Django 4.2.7 on 2023-11-22 21:15

import blog.customs
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/', validators=[blog.customs.validate_file_size]),
        ),
    ]
