# Generated by Django 4.0.6 on 2022-11-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0014_remove_followrs_phone_alter_followrs_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followrs',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
