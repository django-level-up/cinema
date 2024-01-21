# Generated by Django 5.0.1 on 2024-01-21 01:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_seasonsource_valid_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='seasonsource',
            name='show',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.show'),
        ),
        migrations.AlterUniqueTogether(
            name='seasonsource',
            unique_together={('source', 'show', 'season')},
        ),
        migrations.AlterUniqueTogether(
            name='showsource',
            unique_together={('source', 'show')},
        ),
    ]
