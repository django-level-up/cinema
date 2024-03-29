# Generated by Django 5.0.1 on 2024-01-22 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_episodesource_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='episodesource',
            unique_together={('source', 'episode')},
        ),
        migrations.RemoveField(
            model_name='season',
            name='season_sources',
        ),
        migrations.RemoveField(
            model_name='episodesource',
            name='season',
        ),
    ]
