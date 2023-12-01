# Generated by Django 4.2.7 on 2023-11-23 09:53

import blog.customs
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('header_image', models.ImageField(upload_to='images/post', validators=[blog.customs.validate_file_size])),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('status_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(default=[1], related_name='posts', to='blog.category')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
