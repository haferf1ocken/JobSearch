# Generated by Django 2.2.6 on 2019-11-14 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191114_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employer',
            options={'verbose_name_plural': 'employers'},
        ),
        migrations.AlterModelOptions(
            name='intership',
            options={'verbose_name_plural': 'intersips'},
        ),
    ]
