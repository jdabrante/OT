# Generated by Django 5.0 on 2023-12-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='avatar',
            field=models.ImageField(upload_to='judges/%Y/%m/%d'),
        ),
    ]