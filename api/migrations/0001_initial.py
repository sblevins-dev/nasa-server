# Generated by Django 5.0.6 on 2024-07-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PictureOfDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('explanation', models.TextField()),
                ('hdurl', models.TextField()),
                ('media_type', models.CharField(max_length=50)),
                ('service_version', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('url', models.TextField()),
            ],
        ),
    ]
