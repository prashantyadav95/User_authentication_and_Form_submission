# Generated by Django 4.0.6 on 2023-01-07 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_report_reported_by_id_alter_report_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='date',
        ),
        migrations.RemoveField(
            model_name='report',
            name='time',
        ),
    ]
