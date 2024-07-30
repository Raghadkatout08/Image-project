# Generated by Django 5.0.7 on 2024-07-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageURL', models.CharField(max_length=900)),
                ('tags', models.CharField(max_length=200)),
                ('views', models.IntegerField()),
                ('downloads', models.IntegerField()),
                ('collections', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
