# Generated by Django 3.0.9 on 2020-08-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_remove_actor_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='url',
            field=models.SlugField(default='', max_length=160),
        ),
    ]
