# Generated by Django 2.2.7 on 2019-11-16 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191114_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='intership',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='user id'),
        ),
    ]
