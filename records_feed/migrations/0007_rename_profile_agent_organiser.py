# Generated by Django 3.2 on 2022-04-13 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records_feed', '0006_auto_20220413_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='profile',
            new_name='organiser',
        ),
    ]
