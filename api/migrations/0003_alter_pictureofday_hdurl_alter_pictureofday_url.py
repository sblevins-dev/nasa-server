# Generated by Django 5.0.6 on 2024-07-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_pictureofday_copyright'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictureofday',
            name='hdurl',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='pictureofday',
            name='url',
            field=models.URLField(),
        ),
    ]
