# Generated by Django 3.0.9 on 2020-08-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20200805_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='url',
        ),
    ]
