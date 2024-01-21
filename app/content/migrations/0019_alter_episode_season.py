# Generated by Django 5.0.1 on 2024-01-21 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_alter_season_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='content.season'),
        ),
    ]
