# Generated by Django 5.0 on 2023-12-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
                ('city', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('hobbies', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to='media/%Y/%m/%d')),
                ('music_styles', models.ManyToManyField(to='competitors.musicstyle')),
            ],
            options={
                'ordering': ['first_name'],
                'indexes': [models.Index(fields=['first_name'], name='competitors_first_n_a35d1b_idx')],
            },
        ),
    ]