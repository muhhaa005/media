# Generated by Django 5.1.5 on 2025-01-25 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0009_remove_actor_genre_remove_director_genre_genre_actor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='actor',
        ),
    ]
