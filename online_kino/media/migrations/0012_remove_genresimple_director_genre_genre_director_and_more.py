# Generated by Django 5.1.5 on 2025-01-25 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0011_remove_genre_director_genresimple'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genresimple',
            name='director_genre',
        ),
        migrations.AddField(
            model_name='genre',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_genre', to='media.director'),
        ),
        migrations.AddField(
            model_name='genresimple',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_genre_simple', to='media.director'),
        ),
    ]
