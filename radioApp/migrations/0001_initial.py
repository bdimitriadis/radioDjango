# Generated by Django 2.0.1 on 2018-03-12 21:17

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=80)),
                ('areaUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationUrl', models.URLField()),
                ('name', models.CharField(max_length=80)),
                ('images', django.contrib.postgres.fields.jsonb.JSONField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radioApp.Area')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radioApp.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radioApp.Location'),
        ),
    ]
