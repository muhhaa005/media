# Generated by Django 5.1.5 on 2025-01-25 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_actor_country_alter_movie_actor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='director',
        ),
        migrations.AddField(
            model_name='actor',
            name='genre_actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.genre'),
        ),
        migrations.AddField(
            model_name='director',
            name='genre_director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.genre'),
        ),
        migrations.AlterField(
            model_name='favoritemovie',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='media.favorite'),
        ),
        migrations.AlterField(
            model_name='movielanguages',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='language_movie', to='media.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_movie', to='media.movie'),
        ),
    ]
