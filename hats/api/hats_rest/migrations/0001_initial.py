# Generated by Django 4.0.3 on 2022-12-03 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet_name', models.CharField(max_length=100)),
                ('section_number', models.PositiveSmallIntegerField()),
                ('shelf_number', models.PositiveSmallIntegerField()),
                ('import_href', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabric', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('picture_url', models.URLField(max_length=1000, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hats', to='hats_rest.locationvo')),
            ],
            options={
                'ordering': ('style', 'color', 'fabric'),
            },
        ),
    ]