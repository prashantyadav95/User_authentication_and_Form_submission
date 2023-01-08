# Generated by Django 4.0.6 on 2023-01-06 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location1', models.CharField(max_length=20)),
                ('location2', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('security', models.CharField(max_length=50)),
                ('cause', models.CharField(max_length=50)),
                ('action', models.CharField(max_length=50)),
                ('type_env', models.CharField(max_length=20)),
                ('type_inju', models.CharField(max_length=20)),
                ('type_property', models.CharField(max_length=20)),
                ('type_vehicle', models.CharField(max_length=20)),
                ('submitted', models.CharField(max_length=20)),
                ('reported_by_id', models.IntegerField(unique=True)),
            ],
        ),
    ]