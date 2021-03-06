# Generated by Django 3.2.4 on 2022-02-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterSixty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('propagate_date', models.CharField(max_length=256)),
                ('last_value', models.CharField(max_length=256)),
                ('change', models.CharField(max_length=256)),
                ('precent', models.CharField(max_length=256)),
                ('max_value', models.CharField(max_length=256)),
                ('min_value', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ClusterTen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('propagate_date', models.CharField(max_length=256)),
                ('last_value', models.CharField(max_length=256)),
                ('change', models.CharField(max_length=256)),
                ('precent', models.CharField(max_length=256)),
                ('max_value', models.CharField(max_length=256)),
                ('min_value', models.CharField(max_length=256)),
            ],
        ),
    ]
