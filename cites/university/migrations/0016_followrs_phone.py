# Generated by Django 4.0.6 on 2022-12-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0015_alter_followrs_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='followrs',
            name='phone',
            field=models.IntegerField(default=1, unique=True, verbose_name='phone'),
            preserve_default=False,
        ),
    ]
