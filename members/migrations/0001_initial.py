# Generated by Django 4.2.7 on 2023-11-27 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to='judge/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('avatar', models.ImageField(upload_to='teacher/%Y/%m/%d')),
            ],
            options={
                'ordering': ['first_name'],
                'indexes': [models.Index(fields=['first_name'], name='members_tea_first_n_8a1fb1_idx')],
            },
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('birthdate', models.DateTimeField()),
                ('subject', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('hobbies', models.TextField()),
                ('avatar', models.ImageField(upload_to='competitor/%Y/%m/%d')),
                ('music_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitors', to='music.musicstyle')),
            ],
            options={
                'ordering': ['first_name'],
                'indexes': [models.Index(fields=['first_name'], name='members_com_first_n_0edc8b_idx')],
            },
        ),
    ]
