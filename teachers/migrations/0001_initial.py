# Generated by Django 5.0 on 2023-12-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to='media/%Y/%m/%d')),
            ],
            options={
                'ordering': ['first_name'],
                'indexes': [models.Index(fields=['first_name'], name='teachers_te_first_n_24f646_idx')],
            },
        ),
    ]
