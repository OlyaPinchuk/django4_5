# Generated by Django 3.1.7 on 2021-03-30 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,20}$', 'name mush be only a-z A-Z, min 2 and max 20 chars')])),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(150)])),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(blank=True, default='male', max_length=20)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'db_table': 'users',
            },
        ),
    ]
