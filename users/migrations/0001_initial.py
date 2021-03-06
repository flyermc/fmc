# Generated by Django 2.1.2 on 2018-10-30 13:32

from django.db import migrations, models
import django.utils.timezone
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, validators=[users.validators.AsteriskRestrictedEmailValidator], verbose_name='email address')),
                ('password', models.CharField(blank=True, max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='date updated')),
                ('uuid', models.CharField(blank=True, max_length=36, null=True, verbose_name='user uuid')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
            ],
        ),
    ]
