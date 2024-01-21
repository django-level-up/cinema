# Generated by Django 5.0.1 on 2024-01-21 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_moviesource_tmdb_link_showsource_tmdb_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdb_rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='show',
            name='tmdb_rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
