# Generated by Django 3.0.9 on 2020-08-06 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_delete_genreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=1990, max_length=4),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='film_category', to='movie.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='film_genre', to='movie.Genre', verbose_name='жанры'),
        ),
    ]