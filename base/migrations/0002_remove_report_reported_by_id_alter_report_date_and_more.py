# Generated by Django 4.0.6 on 2023-01-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='reported_by_id',
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.TimeField(),
        ),
    ]
