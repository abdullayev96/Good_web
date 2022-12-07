# Generated by Django 4.0.6 on 2022-11-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0011_alter_followrs_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followrs',
            name='email',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='followrs',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='followrs',
            name='phone',
            field=models.IntegerField(unique=True, verbose_name='phone'),
        ),
    ]
