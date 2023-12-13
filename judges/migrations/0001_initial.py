# Generated by Django 5.0 on 2023-12-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200, null=True)),
                ('avatar', models.ImageField(upload_to='judges/%Y/%m/%d')),
            ],
            options={
                'ordering': ['first_name'],
                'indexes': [models.Index(fields=['first_name'], name='judges_judg_first_n_6672e2_idx')],
            },
        ),
    ]
