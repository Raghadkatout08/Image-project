# Generated by Django 5.0.7 on 2024-07-29 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='pageURL',
            new_name='largeImageURL',
        ),
    ]