# Generated by Django 4.0.6 on 2022-08-17 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0011_rename_user_profile_custum_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='custum_user',
            new_name='user',
        ),
    ]
