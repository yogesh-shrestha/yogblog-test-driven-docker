# Generated by Django 4.2.7 on 2023-11-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(),
        ),
    ]
