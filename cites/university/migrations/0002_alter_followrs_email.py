# Generated by Django 4.0.6 on 2022-07-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followrs',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]
