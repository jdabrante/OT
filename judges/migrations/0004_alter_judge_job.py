# Generated by Django 5.0 on 2023-12-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judges', '0003_judge_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='job',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
