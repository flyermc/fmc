# Generated by Django 2.1.2 on 2018-11-06 13:13

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='date_created')),
                ('uuid', models.CharField(blank=True, max_length=36, null=True, verbose_name='user uuid')),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to='images', verbose_name='photo')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=8000, verbose_name='description')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date_updated')),
            ],
        ),
    ]
